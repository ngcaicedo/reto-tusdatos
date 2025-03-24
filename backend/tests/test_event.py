from sqlalchemy import inspect


def test_model_event(db):
    """ Test para verificar que el modelo Event se haya creado correctamente """
    inspector = inspect(db.bind)
    table_names = inspector.get_table_names()
    assert "events" in table_names
