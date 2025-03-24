from sqlalchemy import inspect


def test_model_session(db):
    inspector = inspect(db.bind)
    table_names = inspector.get_table_names()
    assert "sessions" in table_names

def test_model_speaker(db):
    inspector = inspect(db.bind)
    table_names = inspector.get_table_names()
    assert "speakers" in table_names