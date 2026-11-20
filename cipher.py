def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift

    result = ""

    for char in text:
        if 'a' <= char <= 'z':
            base = ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)

        elif 'A' <= char <= 'Z':
            base = ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)

        else:
            result += char

    return result


def brute_force(text):
    results = []

    for shift in range(26):
        results.append({
            "shift": shift,
            "text": caesar_cipher(text, shift, decrypt=True)
        })

    return results
