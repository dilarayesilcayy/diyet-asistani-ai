import os
import sqlite3
import tempfile
import unittest

import database
from auth import login_user, register_user


class AuthenticationTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        database.DB_NAME = os.path.join(self.temp_dir.name, "test.db")
        database.create_tables()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_registration_hashes_password_and_login_succeeds(self):
        success, _ = register_user("dilara_test", "guvenli-test-sifresi")
        self.assertTrue(success)

        with sqlite3.connect(database.DB_NAME) as connection:
            stored_password = connection.execute(
                "SELECT password FROM users WHERE username = ?",
                ("dilara_test",),
            ).fetchone()[0]

        self.assertNotEqual(stored_password, "guvenli-test-sifresi")
        self.assertTrue(stored_password.startswith("pbkdf2_sha256$"))
        self.assertEqual(login_user("dilara_test", "guvenli-test-sifresi")[1], "dilara_test")
        self.assertIsNone(login_user("dilara_test", "yanlis-sifre"))

    def test_registration_rejects_short_credentials(self):
        success, _ = register_user("ab", "12345678")
        self.assertFalse(success)

        success, _ = register_user("valid_user", "short")
        self.assertFalse(success)


if __name__ == "__main__":
    unittest.main()
