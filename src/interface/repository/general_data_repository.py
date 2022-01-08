from abc import ABCMeta, abstractmethod

class GeneralDataRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_general_data(self) -> dict :
        raise NotImplementedError