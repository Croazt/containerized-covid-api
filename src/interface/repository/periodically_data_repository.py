from abc import ABCMeta, abstractmethod

class PeriodicallyDataRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_data(self, since, upto) :
        raise NotImplementedError