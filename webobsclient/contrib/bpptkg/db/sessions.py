from contextlib import contextmanager

from sqlalchemy.orm import scoped_session, sessionmaker


def load_session(engine):
    """Create a new scoped session of current engine."""
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    return Session


@contextmanager
def session_scope(engine):
    session = load_session(engine)
    try:
        yield session()
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.remove()
