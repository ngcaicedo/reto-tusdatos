from sqlalchemy import inspect


def test_model_user(db):
    """ Test para verificar que el modelo User se haya creado correctamente """
    inspector = inspect(db.bind)
    table_names = inspector.get_table_names()
    assert "users" in table_names
