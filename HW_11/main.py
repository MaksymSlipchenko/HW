from abc import ABC, abstractmethod


# 1
class Example:

    @abstractmethod
    def put(self):
        return


example = Example()


# 2
class Example_1(ABC):
    pass


example_1 = Example_1()


# 3
class Example_2(ABC):

    @abstractmethod
    def get(self):
        return


class Example_3(Example_2):

    def get(self):
        return


example_3 = Example_3()
