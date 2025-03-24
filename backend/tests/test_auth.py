def test_hash_password():
    """ Test para verificar que la contraseña se encripta correctamente """
    password = "password"
    hashed_password = hash_password(password)
    assert verify_password(hashed_password, password)