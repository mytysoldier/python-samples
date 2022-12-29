from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int

user = User('sato', 10)
# user.age = 20

user1 = User('sato', 10)
print(user == user1)