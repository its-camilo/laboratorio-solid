"""
Exercise 4 - Interface Segregation Principle (ISP)

The original VehicleActions interface forced every vehicle to implement
irrelevant actions. A GasCar does not pedal or fly, and a Bicycle does not
refuel or fly. The focused interfaces below let each class implement only
the capabilities it actually supports.

YOUR TASK:
  1. Replace the one fat `VehicleActions` interface with several small,
     focused ones: `Movable` (move), `Refuelable` (refuel), `Flyable`
     (fly), `Pedalable` (pedal_harder) -- each with exactly ONE abstract
     method.
  2. Make GasCar implement only Movable + Refuelable, and Bicycle only
     Movable + Pedalable. Remove their now-unnecessary
     NotImplementedError stubs entirely.
  3. Add a new `Drone` class that implements Movable + Flyable (move()
     and fly()) -- and nothing else. It should NOT be forced to
     implement refuel() or pedal_harder().

Run it to see the race once Drone exists:
    python -m exercises.ex4_isp

Check your work:
    pytest tests/test_ex4_isp.py -v
"""
from abc import ABC, abstractmethod

from engine.track import Track


class Movable(ABC):
    @abstractmethod
    def move(self) -> None: ...


class Refuelable(ABC):
    @abstractmethod
    def refuel(self) -> None: ...


class Flyable(ABC):
    @abstractmethod
    def fly(self) -> None: ...


class Pedalable(ABC):
    @abstractmethod
    def pedal_harder(self) -> None: ...


class GasCar(Movable, Refuelable):
    symbol = "\U0001F697"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 4

    def refuel(self):
        print(f"{self.name} refuels at the gas station.")

class Bicycle(Movable, Pedalable):
    symbol = "\U0001F6B2"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 3

    def pedal_harder(self):
        self.position += 1
        print(f"{self.name}'s rider pedals harder!")


class Drone(Movable, Flyable):
    symbol = "\U0001F6F8"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 5

    def fly(self):
        print(f"{self.name} takes off!")


def main():
    vehicles = [GasCar("Racer"), Bicycle("Pedal Pete"), Drone("Sky Scout")]
    Track(length=30).run(vehicles)


if __name__ == "__main__":
    main()
