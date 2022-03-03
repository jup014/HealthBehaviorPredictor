from datetime import datetime
from typing import List, Optional, TypeVar, Generic
from pydantic import BaseModel
from pydantic.generics import GenericModel

class User(BaseModel):
    username: str

TypeX = TypeVar('TypeX')

class DataPoint(GenericModel, Generic[TypeX]):
    timestamp: datetime
    type: str
    value: TypeX

class Data(BaseModel):
    user: User
    data: List[DataPoint] = []

    def add_datapoint(self, timestamp: datetime, type: str, value):
        if isinstance(value, int):
            datapoint = DataPoint[int](timestamp=timestamp, type=type, value=value)
        elif isinstance(value, float):
            datapoint = DataPoint[float](timestamp=timestamp, type=type, value=value)
        else:
            raise TypeError("DataPoint value must be int or float")

        self.data.append(datapoint)



