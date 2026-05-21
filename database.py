# SQLite veritabanı işlemleri burada geliştirilecek.
import sqlite3

DB_NAME = "diyet_asistani.db"


def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def _ensure_column(cursor, table_name, column_name, column_type):
    """
    Tablo varsa ve kolon eksikse ekler.
    Bu sayede eski veritabanı dosyalarında da uygulama patlamaz.
    """
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [col[1] for col in cursor.fetchall()]

    if column_name not in columns:
        cursor.execute(
            f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}"
        )


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # ---------------- users ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        ad_soyad TEXT,
        yas INTEGER,
        cinsiyet TEXT,
        boy REAL,
        gelir TEXT,
        beslenme_tipi TEXT,
        alerjiler TEXT,
        sevilmeyenler TEXT,
        spor_gecmisi TEXT,
        egzersiz_tercihi TEXT,
        egzersiz_hedefi TEXT
    )
    """)

    # Sonradan eklenen kolonları güvenli biçimde ekle
    _ensure_column(cursor, "users", "aktivite", "TEXT")

    # ---------------- weight_logs ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weight_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        kilo REAL NOT NULL,
        tarih TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

    # ---------------- daily_logs ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS daily_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        tarih TEXT NOT NULL,
        su REAL,
        uyku REAL,
        adim INTEGER,
        egzersiz_kalori REAL,
        alinan_kalori REAL,
        gunluk_puan TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

    # ---------------- meal_logs ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS meal_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        tarih TEXT NOT NULL,
        ogun_tipi TEXT,
        yemek_adi TEXT,
        kalori REAL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()


def save_user_profile(
    user_id,
    ad_soyad,
    yas,
    cinsiyet,
    boy,
    gelir,
    beslenme_tipi,
    alerjiler,
    sevilmeyenler,
    spor_gecmisi,
    egzersiz_tercihi,
    egzersiz_hedefi,
    aktivite
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE users
    SET
        ad_soyad = ?,
        yas = ?,
        cinsiyet = ?,
        boy = ?,
        gelir = ?,
        beslenme_tipi = ?,
        alerjiler = ?,
        sevilmeyenler = ?,
        spor_gecmisi = ?,
        egzersiz_tercihi = ?,
        egzersiz_hedefi = ?,
        aktivite = ?
    WHERE id = ?
    """, (
        ad_soyad,
        yas,
        cinsiyet,
        boy,
        gelir,
        beslenme_tipi,
        alerjiler,
        sevilmeyenler,
        spor_gecmisi,
        egzersiz_tercihi,
        egzersiz_hedefi,
        aktivite,
        user_id
    ))

    conn.commit()
    conn.close()


def get_user_profile(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        ad_soyad,
        yas,
        cinsiyet,
        boy,
        gelir,
        beslenme_tipi,
        alerjiler,
        sevilmeyenler,
        spor_gecmisi,
        egzersiz_tercihi,
        egzersiz_hedefi,
        aktivite
    FROM users
    WHERE id = ?
    """, (user_id,))

    row = cursor.fetchone()
    conn.close()

    if not row:
        return None

    return {
        "ad_soyad": row[0] or "",
        "yas": row[1] or 22,
        "cinsiyet": row[2] or "Kadın",
        "boy": row[3] or 169,
        "gelir": row[4] or "Orta",
        "beslenme_tipi": row[5] or "Normal",
        "alerjiler": row[6] or "",
        "sevilmeyenler": row[7] or "",
        "spor_gecmisi": row[8] or "Başlangıç",
        "egzersiz_tercihi": row[9] or "Yürüyüş",
        "egzersiz_hedefi": row[10] or "Yağ Kaybı",
        "aktivite": row[11] or "Düşük"
    }


def add_weight(user_id, kilo, tarih):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO weight_logs (user_id, kilo, tarih)
    VALUES (?, ?, ?)
    """, (user_id, kilo, tarih))

    conn.commit()
    conn.close()


def get_last_weight(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT kilo
    FROM weight_logs
    WHERE user_id = ?
    ORDER BY id DESC
    LIMIT 1
    """, (user_id,))

    row = cursor.fetchone()
    conn.close()

    return row[0] if row else None


def save_daily_log(user_id, tarih, su, uyku, adim, egzersiz_kalori, alinan_kalori, gunluk_puan):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO daily_logs (
        user_id, tarih, su, uyku, adim, egzersiz_kalori, alinan_kalori, gunluk_puan
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (user_id, tarih, su, uyku, adim, egzersiz_kalori, alinan_kalori, gunluk_puan))

    conn.commit()
    conn.close()


def get_last_daily_log(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT tarih, su, uyku, adim, egzersiz_kalori, alinan_kalori, gunluk_puan
    FROM daily_logs
    WHERE user_id = ?
    ORDER BY id DESC
    LIMIT 1
    """, (user_id,))

    row = cursor.fetchone()
    conn.close()

    if not row:
        return None

    return {
        "tarih": row[0],
        "su": row[1] or 0,
        "uyku": row[2] or 0,
        "adim": row[3] or 0,
        "egzersiz_kalori": row[4] or 0,
        "alinan_kalori": row[5] or 0,
        "gunluk_puan": row[6] or "-"
    }


def save_meal_log(user_id, tarih, ogun_tipi, yemek_adi, kalori):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO meal_logs (user_id, tarih, ogun_tipi, yemek_adi, kalori)
    VALUES (?, ?, ?, ?, ?)
    """, (user_id, tarih, ogun_tipi, yemek_adi, kalori))

    conn.commit()
    conn.close()


def get_today_meals(user_id, tarih):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT ogun_tipi, yemek_adi, kalori
    FROM meal_logs
    WHERE user_id = ? AND tarih = ?
    ORDER BY id DESC
    """, (user_id, tarih))

    rows = cursor.fetchall()
    conn.close()

    return rows
def get_weight_history(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT tarih, kilo
    FROM weight_logs
    WHERE user_id = ?
    ORDER BY tarih ASC
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    return rows