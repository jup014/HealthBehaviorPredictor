import datetime

class User:
    def __init__(self, username):
        self.username = username

class TimeSeries:
    def __init__(self, start_time, data_list, time_unit=datetime.timedelta(days=1)):
        self.start_time = start_time
        self.data_list = data_list
        self.time_unit = time_unit

class AdditionalInfoType:
    def __init__(self, typename, options=None):
        self.typename = typename
        self.options = options

class AdditionalInfo:
    def __init__(self, typename, starttime, value):
        self.typename = typename
        self.starttime = starttime
        self.value = value

class HealthBehaviorPredictionContext:
    def add_additional_info(self, typename, starttime, value):
        pass