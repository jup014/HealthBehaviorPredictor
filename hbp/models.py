from datetime import datetime
from typing import List, Optional, TypeVar, Generic
from pydantic import BaseModel
from pydantic.generics import GenericModel

class User(BaseModel):
    username: str

TypeX = TypeVar('TypeX')

class DataPoint(GenericModel, Generic[TypeX]):
    timestamp: datetime
    value: TypeX

class Data(BaseModel):
    user: User
    data: List[DataPoint] = []

    def add_datapoint(self, timestamp: datetime, value):
        if isinstance(value, int):
            datapoint = DataPoint[int](timestamp=timestamp, value=value)
        elif isinstance(value, float):
            datapoint = DataPoint[float](timestamp=timestamp, value=value)
        else:
            raise TypeError("DataPoint value must be int or float")

        self.data.append(datapoint)



