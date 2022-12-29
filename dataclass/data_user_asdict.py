import dataclasses

@dataclasses.dataclass
class User:
    name: str

user = User('sato')
result = dataclasses.asdict(user)
print(result)