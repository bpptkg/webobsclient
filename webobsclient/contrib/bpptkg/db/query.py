from sqlalchemy import func

from ..utils.sqlalchemy import (get_proxy_result_as_dict_with_keys,
                                object_as_dict)
from .sessions import session_scope


def get_bulletin_all_by_range(engine, table, starttime, endtime):
    """
    Get bulletin by particular time range and all event types except None.

    :param engine: SQLAlchemy engine.

    :type engine: :class:`sqlalchemy.engine.base.Engine`

    :param table: SQLAlchemy model or table.

    :param starttime: Start time of the query.

    :type starttime: datetime.datetime

    :param endtime: End time of the query.

    :type endtime: datetime.datetime

    :return: List of dictionary of the events.

    :rtype: list
    """
    with session_scope(engine) as session:
        queryset = session.query(table).filter(
            table.eventdate >= starttime,
            table.eventdate < endtime,
            table.eventtype != None,
        ).order_by(table.eventdate)

        results = queryset.all()
        return [object_as_dict(item) for item in results]


def get_bulletin_by_range(engine, table, starttime, endtime, eventtype):
    """
    Get bulletin by particular time range and eventtype. If eventtype is None,
    query all events.

    :param engine: SQLAlchemy engine.

    :type engine: :class:`sqlalchemy.engine.base.Engine`

    :param table: SQLAlchemy model or table.

    :param starttime: Start time of the query.

    :type starttime: datetime.datetime

    :param endtime: End time of the query.

    :type endtime: datetime.datetime

    :param eventtype: Event type, e.g. VTA, VTB, MP. If you want to query
    multiple eventtypes, pass a list or tuple. If eventtype is None, query all
    events (excluding None).

    :type eventtype: str, list, tuple, or None

    :return: List of dictionary of the events.

    :rtype: list
    """
    with session_scope(engine) as session:
        queryset = session.query(table).filter(
            table.eventdate >= starttime,
            table.eventdate < endtime,
        )
        if isinstance(eventtype, str):
            queryset = queryset.filter(table.eventtype == eventtype)
        elif isinstance(eventtype, (list, tuple)):
            queryset = queryset.filter(table.eventtype.in_(eventtype))
        else:
            queryset = queryset.filter(table.eventtype != None)

        results = queryset.order_by(table.eventdate).all()
        return [object_as_dict(item) for item in results]


def get_bulletin_by_id(engine, table, eventid):
    """
    Get bulletin by its eventid. If not found, return None.

    param engine: SQLAlchemy engine.

    :type engine: :class:`sqlalchemy.engine.base.Engine`

    :param table: SQLAlchemy model or table.

    :param eventid: Event ID, e.g. 2021-07#3414.

    :type eventid: str

    :return: Dictionary of event if exists. Otherwise, return None.

    :rtype: dict or None
    """
    with session_scope(engine) as session:
        queryset = session.query(table).get(eventid)

        return object_as_dict(queryset) if queryset is not None else None


def get_seismicity_all_by_range(engine, table, starttime, endtime):
    """
    Get seismicity by particular time range and all event types except None.

    :param engine: SQLAlchemy engine.

    :type engine: :class:`sqlalchemy.engine.base.Engine`

    :param table: SQLAlchemy model or table.

    :param starttime: Start time of the query.

    :type starttime: datetime.datetime

    :param endtime: End time of the query.

    :type endtime: datetime.datetime

    :return: List of dictionary of the events.

    :rtype: list
    """
    with session_scope(engine) as session:
        subqueryset = session.query(
            table.eventdate.distinct().label('eventdate'),
            table.eventtype.label('eventtype'),
        ).filter(
            table.eventtype != None,
            table.eventdate >= starttime,
            table.eventdate < endtime,
        ).subquery()

        queryset = session.query(
            func.date(subqueryset.c.eventdate).label('timestamp'),
            func.count(subqueryset.c.eventtype).label('count')
        ).group_by(
            func.date(subqueryset.c.eventdate)
        ).order_by(func.date(subqueryset.c.eventdate))

        return get_proxy_result_as_dict_with_keys(
            engine,
            queryset,
            ['timestamp', 'count'],
        )


def get_seismicity_by_range(engine, table, starttime, endtime, eventtype):
    """
    Get seismicity by particular time range and event type.

    :param engine: SQLAlchemy engine.

    :type engine: :class:`sqlalchemy.engine.base.Engine`

    :param table: SQLAlchemy model or table.

    :param starttime: Start time of the query.

    :type starttime: datetime.datetime

    :param endtime: End time of the query.

    :type endtime: datetime.datetime

    :param eventtype: Event type, e.g. VTA, VTB, MP.

    :type eventtype: str

    :return: List of dictionary of the events.

    :rtype: list
    """
    with session_scope(engine) as session:
        subqueryset = session.query(
            table.eventdate.distinct().label('eventdate'),
            table.eventtype.label('eventtype'),
        ).filter(
            table.eventtype == eventtype,
            table.eventdate >= starttime,
            table.eventdate < endtime,
        ).subquery()

        queryset = session.query(
            func.date(subqueryset.c.eventdate).label('timestamp'),
            func.count(subqueryset.c.eventtype).label('count')
        ).group_by(
            func.date(subqueryset.c.eventdate)
        ).order_by(func.date(subqueryset.c.eventdate))

        return get_proxy_result_as_dict_with_keys(
            engine,
            queryset,
            ['timestamp', 'count'],
        )


def filter_not_exists(engine, table, events):
    """
    Generator function to check if particular event is not exists in the
    database. If not exists, yield event.
    """
    with session_scope(engine) as session:
        for event in events:
            result = session.query(table).get(event['eventid'])
            if result is None:
                yield event


def filter_exists(engine, table, events):
    """
    Generator function to check if particular event is exists in the database.
    If exists, yield tuple of event and the result from the database.
    """
    with session_scope(engine) as session:
        for event in events:
            result = session.query(table).get(event['eventid'])
            if result is not None:
                yield (event, result)


def filter_exact(engine, table, events):
    """
    Generator function to check if particular event is not exists (event ID not
    exists, or event ID exists but eventtype differ) in the database. If the
    criteria matched, yield tuple of event and the result from the database.
    """
    with session_scope(engine) as session:
        for event in events:
            obj = session.query(table).get(event['eventid'])
            result = object_as_dict(obj) if obj is not None else None
            if (
                (result is None)
                or (
                    result is not None
                    and result['eventtype'] != event['eventtype']
                )
            ):
                yield (event, result)
