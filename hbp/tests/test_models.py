from datetime import datetime, timedelta
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
        datapoint = DataPoint[float](timestamp=datetime.now(), type="steps per day", value=1.0)
        self.assertEqual(datapoint.value, 1.0)

        datapoint2 = DataPoint[int](timestamp=datetime.now(), type="steps per day", value=1)
        self.assertEqual(datapoint2.value, 1)

        self.assertRaises(TypeError, DataPoint[str], timestamp=datetime.now(), type="steps per day", value="1")

    def test_data_add_datapoint(self):
        user = User(username="testuser")
        data = Data(user=user)
        data.add_datapoint(datetime.now(), "steps per day", 1.0)

    def test_data_add_datapoint_list(self):
        user = User(username="testuser")
        data = Data(user=user)
        data.add_datapoint_list(datetime.now(), "steps per day", [1, 2, 3], timedelta(days=1))
        self.assertEqual(len(data.datapoints), 3)
        self.assertEqual(data.datapoints[0].value, 1)
        self.assertEqual(data.datapoints[1].value, 2)
        self.assertEqual(data.datapoints[2].value, 3)
