from dataclasses import dataclass


@dataclass
class User:
    tg_id: int
    address: str
    phone: str
