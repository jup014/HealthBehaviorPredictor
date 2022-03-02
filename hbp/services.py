import datetime

class HealthBehaviorPredictionContext:
  def add_additional_info(self, typename, starttime, value):
    pass

class HealthBehaviorPredictor:
  def add_user(self, username):
    return username
  
  def add_time_series(self, username, starttime, data_list, time_unit=datetime.timedelta(days=1)):
    pass
  
  def train(self):
    pass

  def predict(self, username, predict_time, context_params=None):
    return 1
  
  def add_additional_info_type(self, typename, options=None):
    return typename
  
  def add_additional_info(self, typename, starttime, value):
    pass
  
  def create_prediction_context(self, username) -> HealthBehaviorPredictionContext:
    return HealthBehaviorPredictionContext()

  def predict_with_context(self, username, starttime, context):
    return 1