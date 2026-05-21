# Kullanıcı kayıt ve giriş işlemleri burada geliştirilecek.
from database import get_connection


def register_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        return True, "Kayıt başarılı."
    except Exception:
        return False, "Bu kullanıcı adı zaten kayıtlı olabilir."
    finally:
        conn.close()


def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, username FROM users WHERE username = ? AND password = ?",
        (username, password)
    )
    user = cursor.fetchone()

    conn.close()
    return user