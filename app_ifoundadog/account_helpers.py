import string
import secrets


def generate_password():
    """
    generates strong password of 32 chars with letters, digits, and symbols
    :return: string
    """
    return "".join(
        [
            secrets.choice(
                string.ascii_letters +
                string.digits +
                string.punctuation
            )
            for _ in range(32)
        ]
    )
