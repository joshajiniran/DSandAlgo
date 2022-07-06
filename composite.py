from abc import abstractmethod, ABC


class Component(ABC):
    @abstractmethod
    def component_function(self):
        """Must be implemented"""


class Child(Component):
    def component_function(self):
        return super().component_function()


child = Child()
