import datetime
from hbp.services import HealthBehaviorPredictor

predictor = HealthBehaviorPredictor()

user = predictor.add_user("jp")

predictor.add_time_series(user, datetime.datetime(2022, 3, 2), [1,2,3,4,5,6,7])
predictor.add_time_series(user, datetime.datetime(2022, 3, 9), [1,2,3,4,5,6,7])
predictor.add_time_series(user, datetime.datetime(2022, 3, 16), [1,2,3,4,5,6,7])
predictor.add_time_series(user, datetime.datetime(2022, 3, 23), [1,2,3,4,5,6,7])
predictor.add_time_series(user, datetime.datetime(2022, 3, 30), [1,2,3,4,5,6,7])

weather_type = predictor.add_additional_info_type("weather", ["sunny", "cloudy", "rainy", "snowy"])
predictor.add_additional_info(weather_type, datetime.datetime(2022, 3, 2), "sunny")
predictor.add_additional_info(weather_type, datetime.datetime(2022, 3, 3), "cloudy")

notification_sent = predictor.add_additional_info_type("notification", ["sent", "not sent"])
predictor.add_additional_info(notification_sent, datetime.datetime(2022, 3, 3, 14, 30), "sent")
predictor.add_additional_info(notification_sent, datetime.datetime(2022, 3, 3, 18, 30), "sent")

predictor.train()

predicted_value1 = predictor.predict(user, datetime.datetime(2022, 4, 5))
predicted_value2 = predictor.predict(user, datetime.datetime(2022, 4, 5), {"weather": "sunny"})

prediction_context = predictor.create_prediction_context(user)
prediction_context.add_additional_info(weather_type, datetime.datetime(2022, 4, 5), "sunny")
prediction_context.add_additional_info(notification_sent, datetime.datetime(2022, 4, 5, 9, 0), "sent")

predicted_value3 = predictor.predict_with_context(user, datetime.datetime(2022, 4, 5), prediction_context)
