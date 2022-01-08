from abc import ABCMeta, abstractmethod

class CovidDataDriverInt(metaclass=ABCMeta):
    @abstractmethod
    def get_data_total(self) ->dict:
        raise NotImplementedError
    @abstractmethod
    def get_data(self) ->dict:
        raise NotImplementedError

    @abstractmethod
    def get_data_periodic(self):
        raise NotImplementedError