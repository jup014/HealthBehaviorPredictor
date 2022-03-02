import datetime
from .models import User, TimeSeries, AdditionalInfoType, AdditionalInfo, HealthBehaviorPredictionContext

class HealthBehaviorPredictor:
    def __init__(self):
        self.users = {}
        self.time_series = {}
        self.additional_info_types = {}
        self.additional_info = {}
        self.prediction_contexts = {}

    def add_user(self, username):
        user = User(username)
        self.users[username] = user
        return user

    def add_time_series(self,
                        username,
                        starttime,
                        data_list,
                        time_unit=datetime.timedelta(days=1)):
        time_series = TimeSeries(starttime, data_list, time_unit)
        if username not in self.time_series:
            self.time_series[username] = []
        self.time_series[username].append(time_series)

        return time_series

    def train(self):
        pass

    def predict(self, username, predict_time, context_params=None):
        return 1

    def add_additional_info_type(self, typename, options=None):
        additional_info_type = AdditionalInfoType(typename, options)
        self.additional_info_types[typename] = additional_info_type
        return additional_info_type

    def add_additional_info(self, typename, starttime, value):
        additional_info = AdditionalInfo(typename, starttime, value)
        if typename not in self.additional_info:
            self.additional_info[typename] = []
        self.additional_info[typename].append(additional_info)
        return additional_info

    def create_prediction_context(self,
                                  username) -> HealthBehaviorPredictionContext:
        prediction_context = HealthBehaviorPredictionContext(username)
        if username not in self.prediction_contexts:
            self.prediction_contexts[username] = []
        self.prediction_contexts[username].append(prediction_context)
        return prediction_context

    def predict_with_context(self, username, starttime, context):
        return 1
