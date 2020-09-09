import hashlib
import binascii
import os
import sqlite3
import os.path
import sys


class UsersModal:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.base_dir, "TMS.db")

    @staticmethod
    def hash_password(password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    @staticmethod
    def verify_password(stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    def check_user(self, login_id, password):
        with sqlite3.connect(self.db_path) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM users WHERE login_id=?", (login_id,))
            record = cur.fetchone()
            if record:
                if self.verify_password(record['password'], password):
                    return record
                else:
                    return 'Wrong Password'
            else:
                return 'Invalid Login'

    def insert_user(self, s):
        user_values = (s['email'], s['login_id'], self.hash_password(s['password']), s['type'], s['id'])
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO users(email, login_id, password, type, parent_id) VALUES(?,?,?,?,?)", user_values)
            con.commit()
            return cur.rowcount

# if __name__ == '__main__':
#     x = UsersModal()
#     print(x.db_path)
