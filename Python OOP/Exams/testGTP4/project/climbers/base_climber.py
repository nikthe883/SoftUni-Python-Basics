from abc import ABC, abstractmethod
from peaks.base_peak import BasePeak

class BaseClimber(ABC):
    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks = []
        self.is_prepared = True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Climber name cannot be null or empty!")
        self._name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.__strength = value

    @abstractmethod
    def can_climb(self):
        pass

    @abstractmethod
    def climb(self, peak: 'BasePeak'):
        pass

    def rest(self):
        self.__strength += 15

    def __str__(self):
        peaks = ", ".join(self.conquered_peaks)
        return f"{type(self).__name__}: /// Climber name: {self.name} * Left strength: {round(self.strength, 1)} * Conquered peaks: {peaks} ///"
