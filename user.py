class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.profile = {}

    def update_profile(self, key, value):
        self.profile[key] = value

    def get_profile(self):
        return self.profile