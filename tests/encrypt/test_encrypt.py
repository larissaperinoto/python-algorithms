from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(key="A", message="abc")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(key=1, message=2)

    assert encrypt_message(key=100, message="abc") == "cba"
    assert encrypt_message(key=3, message="pessego") == "sep_oges"
    assert encrypt_message(key=4, message="pessego") == "oge_ssep"
