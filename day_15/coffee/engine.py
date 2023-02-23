from functools import reduce
from typing import List, Optional

from .coffee import Coffee

COINS = {
    "quarter": 25,
    "dime": 10,
    "nickle": 5,
    "penny": 1,
}


class CoffeeMachineEngine:
    def __init__(
        self,
        available_coffees: List[Coffee],
        water: int = 1000,
        milk: int = 600,
        coffee: int = 500,
        money: int = 5000,
    ) -> None:
        self.available_coffees = available_coffees
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money
        self._machine_on: bool = True

    def print_report(self) -> None:
        print(
            f"""
            Water: {self.water}
            Milk: {self.milk}
            Coffee: {self.coffee}
            Money: {self.money}"""
        )

    @property
    def available_drinks(self) -> List[str]:
        return [drink.name for drink in self.available_coffees]

    @property
    def machine_on(self) -> bool:
        return self._machine_on

    @machine_on.setter
    def machine_on(self, state: bool) -> None:
        usr_input = input("Are you sure you want to turn machine off? [Y/N]")
        if usr_input.lower() == "y":
            print("Shutting down.")
            self._machine_on = state

    def check_resources(
        self,
        water: int,
        milk: int,
        coffee: int,
    ) -> bool:
        resources = locals()
        resources.pop("self", None)
        for name, value in resources.items():
            if not (value <= self.__dict__[name]):
                print(f"Sorry, there's not enough {name} ")
                return False
        return True

    def process_coins(
        self,
        quarter: Optional[int] = None,
        dime: Optional[int] = None,
        nickle: Optional[int] = None,
        penny: Optional[int] = None,
    ) -> int:
        resources = locals()
        resources.pop("self", None)
        resources = {
            key: value for key, value in resources.items() if value is not None
        }
        return reduce(
            lambda value, key: value + resources[key] * COINS[f"{key}"], resources, 0
        )

    def get_coffee(self, drink_name: str) -> Coffee:
        for drink in self.available_coffees:
            if drink.name.lower() == drink_name.lower():
                return drink

        raise KeyError("Coffee of that type is not available.")

    def process_drink(self, drink: Coffee, money: int) -> None:
        if self.check_resources(drink.water, drink.milk, drink.coffee):
            self.water -= drink.water
            self.milk -= drink.milk
            self.coffee -= drink.coffee

        if money > drink.price:
            print(f"Your change is: {(money - drink.price)/100:.2f}")

        self.money += drink.price

        print(f"Here's your {drink.name}.")
