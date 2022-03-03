import datetime
from .models import User


class HealthBehaviorPredictor:

    def __init__(self):
        self.user_list = []

    @property
    def __version__(self):
        return '0.0.1'

    def add_user(self, username):
        user = User(username=username)
        self.user_list.append(user)
        return user

    def get_user_list(self):
        return self.user_list