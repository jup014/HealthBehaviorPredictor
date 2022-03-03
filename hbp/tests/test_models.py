from datetime import datetime
from unittest import TestCase
from hbp.models import Data, User, DataPoint

class ModelTest(TestCase):
    def test_main(self):
        self.assertEqual(1, 1)

    def test_user(self):
        user = User(username="testuser")
        self.assertEqual(user.username, "testuser")
    
    def test_data(self):
        user = User(username="testuser")
        data = Data(user=user)

    def test_datapoint(self):
        datapoint = DataPoint[float](timestamp=datetime.now(), value=1.0)
        self.assertEqual(datapoint.value, 1.0)

    def test_data_add_datapoint(self):
        user = User(username="testuser")
        data = Data(user=user)
        data.add_datapoint(datetime.now(), 1.0)