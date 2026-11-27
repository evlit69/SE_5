import pytest


from cipher import brute_force, caesar_cipher, process_cipher
from app import app as flask_app

@pytest.fixture
def client():
    flask_app.config["TESTING"] = True

    with flask_app.test_client() as client:
        yield client


def test_character_and_word_count(client):
    response = client.post("/", data={
        "text": "Hello world!",
        "shift": "3",
        "mode": "encrypt"
    })

    assert b'id="input-char-count">12</span>' in response.data
    assert b'id="input-word-count">2</span>' in response.data


def test_count_multiple_spaces_and_line_breaks(client):
    response = client.post("/", data={
        "text": "Hello   world\nPython",
        "shift": "3",
        "mode": "encrypt"
    })

    assert b'id="input-char-count">20</span>' in response.data
    assert b'id="input-word-count">3</span>' in response.data


def test_empty_input_count(client):
    response = client.post("/", data={
        "text": "",
        "shift": "3",
        "mode": "encrypt"
    })

    assert b'id="input-char-count">0</span>' in response.data
    assert b'id="input-word-count">0</span>' in response.data


def test_encryption_and_decryption_result_count(client):
    for text, mode in [
        ("Hello world!", "encrypt"),
        ("Khoor zruog!", "decrypt")
    ]:
        response = client.post("/", data={
            "text": text,
            "shift": "3",
            "mode": mode
        })

        assert b"Characters: 12</span>" in response.data
        assert b"Words: 2</span>" in response.data


def test_invalid_input_does_not_display_result_count(client):
    response = client.post("/", data={
        "text": "Hello world!",
        "shift": "30",
        "mode": "encrypt"
    })

    assert b"Shift must be an integer between 0 and 25." in response.data
    assert b'id="input-char-count">12</span>' in response.data
    assert b'id="input-word-count">2</span>' in response.data
    assert b'id="result"' not in response.data

def test_encrypt():
    assert caesar_cipher("HELLO", 3) == "KHOOR"


def test_decrypt():
    assert caesar_cipher("KHOOR", 3, decrypt=True) == "HELLO"


def test_preserve_spaces_and_numbers():
    assert caesar_cipher("HELLO 123!", 3) == "KHOOR 123!"


def test_lowercase():
    assert caesar_cipher("hello", 3) == "khoor"


def test_wrap_around():
    assert caesar_cipher("XYZ", 3) == "ABC"


def test_zero_shift():
    assert caesar_cipher("HELLO", 0) == "HELLO"


def test_brute_force():
    results = brute_force("KHOOR")

    assert len(results) == 26
    assert results[3]["text"] == "HELLO"
    assert results[3]["shift"] == 3


def test_unsupported_operation():
    with pytest.raises(ValueError):
        process_cipher("HELLO", 3, "unknown")
