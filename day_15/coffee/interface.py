from .engine import COINS, CoffeeMachineEngine


class CoffeeMachineInterface:
    def __init__(self, engine: CoffeeMachineEngine) -> None:
        self.engine = engine

    def run(self) -> None:
        while self.engine.machine_on:
            user_input = input("Please choose an option: report / order: ").lower()

            if user_input == "report":
                self.engine.print_report()
            elif user_input == "off":
                self.engine.machine_on = False
            elif user_input == "order":
                user_input = input(
                    f"Please choose from list of drinks: {', '.join(self.engine.available_drinks)}: "
                )
                try:
                    drink = self.engine.get_coffee(user_input)
                except KeyError:
                    print("Coffee of that type is not available.")
                    continue
                coins = []
                for coin in COINS:
                    coins.append(int(input(f"Please provide {coin} amount :")))

                money = self.engine.process_coins(*coins)

                if money < drink.price:
                    print("Not enough money provided.")
                else:
                    self.engine.process_drink(drink, money)
                print("Enjoy!")
