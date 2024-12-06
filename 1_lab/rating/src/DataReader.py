# -*- coding: utf-8 -*-
from Types import DataType
from abc import ABC, abstractmethod
import json


class DataReader(ABC):

    @abstractmethod
    def read(self) -> DataType:
        pass
