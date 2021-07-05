from sqlalchemy import inspect


def object_as_dict(obj):
    """
    Convert SQLAlchemy model to dictionary.
    """
    return {
        item.key: getattr(obj, item.key)
        for item in inspect(obj).mapper.column_attrs
    }


def as_dict_with_keys(obj, keys):
    """
    Convert SQLAlchemy model to list of dictionary with provided keys.
    """
    return [dict((a, b) for (a, b) in zip(keys, item)) for item in obj]


def proxy_result_as_dict(obj):
    """
    Convert SQLAlchemy proxy result object to list of dictionary.
    """
    return [{key: value for key, value in row.items()} for row in obj]


def get_proxy_result_as_dict(engine, queryset):
    """
    Get SQLAlchemy proxy result as dictionary.
    """
    sql_expression = queryset.statement.compile(engine)
    result = engine.execute(sql_expression)
    return proxy_result_as_dict(result)


def get_proxy_result_as_dict_with_keys(engine, queryset, keys):
    """
    Get SQLAlchemy proxy result as dictionary with provided keys.
    """
    sql_expression = queryset.statement.compile(engine)
    result = engine.execute(sql_expression).fetchall()
    return as_dict_with_keys(result, keys)
