import hashlib

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS

from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one_user(bid)

    def get_all(self):
        return self.dao.get_all_users()

    def create(self, user_d):
        return self.dao.create(user_d)

    def update(self, user_d):
        return self.dao.update(user_d)

    def delete(self, bid):
        return self.dao.delete(bid)


def get_hash(password):
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),  # Convert the password to bytes
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    ).decode("utf-8", "ignore")
