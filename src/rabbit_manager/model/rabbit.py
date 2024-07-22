import datetime as dt
from decimal import Decimal
from typing import Optional, Any, Dict

from rabbit_manager.utils import common_utils


class Rabbit:
    DATE_FORMAT = '%Y-%m-%d'

    def __init__(self):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.color: Optional[str] = None
        self.weight_kg: Optional[Decimal] = None
        self.height_cm: Optional[Decimal] = None
        self.birth_date: Optional[dt.date] = None

    def validate(self, nullable: bool = False) -> None:
        common_utils.validate_type(self.id, str, nullable=nullable)
        common_utils.validate_type(self.name, str, nullable=nullable)
        common_utils.validate_type(self.color, str, nullable=nullable)
        common_utils.validate_type(self.weight_kg, Decimal, nullable=nullable)
        common_utils.validate_type(self.height_cm, Decimal, nullable=nullable)
        common_utils.validate_type(self.birth_date, dt.date, nullable=nullable)

    def to_dict(self) -> Dict[str, Any]:
        self.validate(nullable=True)

        rabbit_item: Dict[str, Any] = {}
        if self.id is not None:
            rabbit_item['id'] = self.id
        if self.name is not None:
            rabbit_item['name'] = self.name
        if self.color is not None:
            rabbit_item['color'] = self.color
        if self.weight_kg is not None:
            rabbit_item['weightKg'] = str(self.weight_kg)
        if self.height_cm is not None:
            rabbit_item['heightCm'] = str(self.height_cm)
        if self.birth_date is not None:
            rabbit_item['birthDate'] = self.birth_date.strftime(Rabbit.DATE_FORMAT)
        return rabbit_item

    @classmethod
    def from_dict(cls, rabbit_item: Dict[str, Any], request: bool = False):
        rabbit = Rabbit()
        if 'id' in rabbit_item and not request:
            common_utils.validate_type(rabbit_item['id'], str)
            rabbit.id = rabbit_item['id']
        if 'name' in rabbit_item:
            common_utils.validate_type(rabbit_item['name'], str)
            rabbit.name = rabbit_item['name']
        if 'color' in rabbit_item:
            common_utils.validate_type(rabbit_item['color'], str)
            rabbit.color = rabbit_item['color']
        if 'weightKg' in rabbit_item:
            common_utils.validate_type_list(
                rabbit_item['weightKg'],
                (str, Decimal),
            )
            rabbit.weight_kg = rabbit_item['weightKg'] \
                if isinstance(rabbit_item['weightKg'], Decimal) \
                else Decimal(rabbit_item['weightKg'])
        if 'heightCm' in rabbit_item:
            common_utils.validate_type_list(
                rabbit_item['heightCm'],
                (str, Decimal),
            )
            rabbit.height_cm = rabbit_item['heightCm'] \
                if isinstance(rabbit_item['heightCm'], Decimal) \
                else Decimal(rabbit_item['heightCm'])
        if 'birthDate' in rabbit_item and not request:
            common_utils.validate_type(rabbit_item['birthDate'], str)
            rabbit.birth_date = dt.datetime.strptime(
                rabbit_item['birthDate'],
                Rabbit.DATE_FORMAT,
            ).date()
        return rabbit
