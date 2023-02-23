from coffee.coffee import Coffee
from coffee.engine import CoffeeMachineEngine
from coffee.interface import CoffeeMachineInterface


def main() -> None:
    coffees = [
        Coffee("Latte", 50, 250, 40, 250),
        Coffee("Americano", 220, 0, 60, 200),
        Coffee("Flat white", 80, 140, 80, 300),
    ]
    engine = CoffeeMachineEngine(coffees)
    interface = CoffeeMachineInterface(engine)

    interface.run()


if __name__ == "__main__":
    main()
