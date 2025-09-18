from abc import ABC, abstractmethod

class UserRepository(ABC):
    """Handles User data persistence"""

    @abstractmethod
    def saveUser(self, users: dict):
        pass


# Low-Level Modules (Implementations)

class MysqlUserRepository(UserRepository):
    def saveUser(self, user_data: dict):
        print(f"Saving user {user_data['name']} to MySQL database")


class PostgresUserRepository(UserRepository):
    def saveUser(self, user_data: dict):
        print(f"Saving user {user_data['name']} to PostgreSQL database")

class MongoUserRepository(UserRepository):
    def saveUser(self, user_data: dict):
        print(f"Saving user {user_data['name']} to MongoDB database")


# High-Level Module
class UserService:
    """Handles user-related operations"""

    def __init__(self, repository: UserRepository):
        self.users = {}  # pretend database {email: password}
        self.repository = repository

    def registerUser(self, email, password):
        if email in self.users:
            print(f"Registration failed !! User with {email} already existed")
            return
        if "@" not in email or "." not in email:
            print("Registration failed !! Invalid email")
            return
        if len(password) < 5:
            print("Registration failed !! password must be 6 characters long")
            return
        self.users[email] = password
        self.repository.saveUser({
            "name": email.split("@")[0],
            "email": email,
            "password": password
        })
        print(f"User with {email} created")

# Usage:
mysql_repo = MysqlUserRepository()
postgres_repo = PostgresUserRepository()
mongo_repo = MongoUserRepository()


user_service_mysql = UserService(mysql_repo)
user_service_postgres = UserService(postgres_repo)
user_service_mongo = UserService(mongo_repo)

user_service_mysql.registerUser("tahjib@gami.com", "ghjklp")
user_service_mongo.registerUser("user2@gmail.com", "password123")
user_service_postgres.registerUser("user3@gmail.com" , "mypassword")