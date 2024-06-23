"""user模块，用于处理用户相关的操作"""

from peewee import *
from werkzeug.security import generate_password_hash, check_password_hash

# MySQL 数据库连接设置
db = MySQLDatabase('your_database_name', user='your_username', password='your_password', host='localhost', port=3306)


class BaseModel(Model):
    class Meta:
        database = db


# 用户模型定义
class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()  # 用于存储加密密码
    real_name = CharField()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __str__(self):
        return f'{self.username} ({self.real_name})'


# 确保在应用启动前执行数据库连接和表创建
def initialize_database():
    db.connect()
    db.create_tables([User], safe=True)


# 可以在这里增加测试数据或其他功能

if __name__ == '__main__':
    initialize_database()
