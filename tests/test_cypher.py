import pytest

from cipher import brute_force, caesar_cipher, process_cipher


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
