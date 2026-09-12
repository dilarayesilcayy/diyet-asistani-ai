import hashlib
import hmac
import os

from database import get_connection


PBKDF2_ITERATIONS = 600_000


def _hash_password(password):
    """Return a versioned PBKDF2 password record."""
    salt = os.urandom(16)
    derived_key = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        PBKDF2_ITERATIONS,
    )
    return (
        f"pbkdf2_sha256$${PBKDF2_ITERATIONS}$"
        f"${salt.hex()}$${derived_key.hex()}"
    )


def _verify_password(password, stored_password):
    """Safely compare a password with a stored PBKDF2 record."""
    try:
        algorithm, iterations, salt_hex, expected_hex = stored_password.split("$", 3)
        if algorithm != "pbkdf2_sha256":
            return False

        derived_key = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            bytes.fromhex(salt_hex),
            int(iterations),
        )
        return hmac.compare_digest(derived_key.hex(), expected_hex)
    except (AttributeError, TypeError, ValueError):
        return False


def _validate_credentials(username, password):
    username = username.strip()

    if len(username) < 3:
        return False, "Kullanıcı adı en az 3 karakter olmalıdır."
    if len(username) > 50:
        return False, "Kullanıcı adı en fazla 50 karakter olabilir."
    if len(password) < 8:
        return False, "Şifre en az 8 karakter olmalıdır."
    if len(password) > 128:
        return False, "Şifre en fazla 128 karakter olabilir."

    return True, ""


def register_user(username, password):
    username = username.strip()
    is_valid, message = _validate_credentials(username, password)
    if not is_valid:
        return False, message

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, _hash_password(password)),
        )
        conn.commit()
        return True, "Kayıt başarılı."
    except Exception:
        return False, "Bu kullanıcı adı kullanılamıyor."
    finally:
        conn.close()


def login_user(username, password):
    username = username.strip()

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, username, password FROM users WHERE username = ?",
        (username,),
    )
    user = cursor.fetchone()
    conn.close()

    if not user or not _verify_password(password, user[2]):
        return None

    return user[0], user[1]
