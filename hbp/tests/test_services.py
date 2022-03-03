from unittest import TestCase
from hbp.models import Data
from hbp.services import HealthBehaviorPredictor

from datetime import datetime

class ServiceTest(TestCase):
    def test_main(self):
        self.assertEqual(1, 1)

    def test_service(self):
        predictor = HealthBehaviorPredictor()
        self.assertEqual(predictor.__version__, '0.0.1')
    
    def test_add_user(self):
        predictor = HealthBehaviorPredictor()
        user = predictor.add_user('test')
        self.assertEqual(user.username, 'test')
        userlist = predictor.get_user_list()
        self.assertEqual(len(userlist), 1)
        self.assertEqual(userlist[0].username, 'test')
    
    def test_add_data(self):
        predictor = HealthBehaviorPredictor()
        user = predictor.add_user('test')
        data = Data(user=user)
        data.add_datapoint(datetime.now(), "daily step data", 1.0)
        predictor.add_data(data)