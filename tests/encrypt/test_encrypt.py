from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(key='A', message='abc')

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(key=1, message=2)

    result1 = encrypt_message(key=100, message='abc')
    odd_key = encrypt_message(key=1, message='abc')
    even_key = encrypt_message(key=2, message='abc')

    assert result1 == 'cba'
    assert odd_key == 'a_cb'
    assert even_key == 'c_ba'

