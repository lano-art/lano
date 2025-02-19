from user_data import UserData
import logging


class UserHandler:
    def __init__(self):
        self.user_data = UserData()
        logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    def create_user(self, username, password):
        if not self.user_data.validate_username(username):
            logging.warning(f"Invalid username: {username}")
            return False, "اسم المستخدم غير صالح"
        if not self.user_data.validate_password(password):
            logging.warning(f"Invalid password for user: {username}")
            return False, "كلمة المرور غير صالحة"

        if self.user_data.add_user(username, password):
            logging.info(f"User created successfully: {username}")
            return True, "تم إنشاء الحساب بنجاح"
        else:
            logging.warning(f"Username already exists: {username}")
            return False, "اسم المستخدم موجود مسبقًا"

    def login_user(self, username, password):
        if self.user_data.verify_user(username, password):
            logging.info(f"User logged in successfully: {username}")
            return True, "تم تسجيل الدخول بنجاح"
        else:
            logging.warning(f"Failed login attempt for user: {username}")
            return False, "اسم المستخدم أو كلمة المرور غير صحيحة"
