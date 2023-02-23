""" Module containing coffee types representations """
from dataclasses import dataclass, field


@dataclass
class Coffee:
    name: str = field(compare=True)
    water: int = field(compare=False)
    milk: int = field(compare=False)
    coffee: int = field(compare=False)
    price: int = field(compare=False)

    @property
    def total_ml(self):
        return self.water + self.milk
