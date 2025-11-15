from user import User
from health import Health

class PersonalHealthCareAgent:
    def __init__(self):
        self.users = {}
        self.health_data = {}

    def register_user(self, username, password):
        self.users[username] = User(username, password)

    def login_user(self, username, password):
        if username in self.users and self.users[username].password == password:
            return self.users[username]
        else:
            return None

    def track_health(self, user, key, value):
        if user.username not in self.health_data:
            self.health_data[user.username] = Health()
        self.health_data[user.username].add_data(key, value)

    def get_recommendations(self, user):
        if user.username in self.health_data:
            return self.health_data[user.username].get_recommendations(user)
        else:
            return []

def main():
    agent = PersonalHealthCareAgent()

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Track Health")
        print("4. Get Recommendations")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            agent.register_user(username, password)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = agent.login_user(username, password)
            if user:
                print("Login successful")
            else:
                print("Invalid credentials")
        elif choice == "3":
            username = input("Enter username: ")
            user = agent.users.get(username)
            if user:
                key = input("Enter health key (e.g., weight, blood_pressure): ")
                value = float(input("Enter health value: "))
                agent.track_health(user, key, value)
            else:
                print("User not found")
        elif choice == "4":
            username = input("Enter username: ")
            user = agent.users.get(username)
            if user:
                recommendations = agent.get_recommendations(user)
                print("Recommendations:")
                for recommendation in recommendations:
                    print(recommendation)
            else:
                print("User not found")
        elif choice == "5":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()