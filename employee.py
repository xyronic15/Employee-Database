from dataclasses import dataclass, asdict
import datetime

@dataclass
class Employee:
    id: int
    first_name: str
    last_name: str 
    date: datetime.date 
    salary: int
    department: str

    def to_json(self):
        return asdict(self)
