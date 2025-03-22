from sqlalchemy import inspect


def test_model_assistant(db):
    inspector = inspect(db.bind)
    table_names = inspector.get_table_names()
    assert "assistants" in table_names
