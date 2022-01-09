from abc import ABCMeta, abstractmethod

class PeriodicallyDataRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_yearly_data(self, since, upto) -> dict :
        raise NotImplementedError