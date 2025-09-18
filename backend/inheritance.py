
class BaseRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create(self, data):
        return f"Creating record with data: {data} into {self.db_connection}"
    
    def get(self, id):
        return f"Getting record with id: {id} from {self.db_connection}"
    
    def update(self, id, data):
        return f"Updating record with id: {id} to data: {data} in {self.db_connection}"
    
    def delete(self, id):
        return f"Deleting record with id: {id} from {self.db_connection}"
    

class UserRepo(BaseRepository):
    def find_by_username(self, username):
        return f"Finding user with username: {username} in {self.db_connection}"
    
    def find_by_email(self, email):
        return f"Finding user with email: {email} in {self.db_connection}"
    
    def get_all_users(self):
        return f"Getting all users from {self.db_connection}"
    

database_connection_type = "PostgreSQL"
user_repo = UserRepo(database_connection_type)


create = user_repo.create("John Doe")
get = user_repo.get(5)
update = user_repo.update(5, "Jane Doe")
delete = user_repo.delete(6)
username = user_repo.find_by_username("johndoe")
email = user_repo.find_by_email("user2@gmail.com")


print(create)
print(get)
print(update)
print(delete)
print(username)
print(email)


