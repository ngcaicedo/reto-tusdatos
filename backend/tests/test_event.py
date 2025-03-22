from sqlalchemy import inspect


def test_model_event(db):
    inspector = inspect(db.bind)
    table_names = inspector.get_table_names()
    assert "events" in table_names
