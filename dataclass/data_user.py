from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    age: int
    items: list[int] = field(default_factory=lambda:['test'])

user = User('sato', 10)
print(user.name)
print(user.age)
print(user.items)