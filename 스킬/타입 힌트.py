name: str = "John Doe"

age: int = 25

# emails: list: ["john1@doe.com", "john2@doe.com"]

address: dict = {
  "street": "54560 Daugherty Brooks Suite 581",
  "city": "Stokesmouth",
  "state": "NM",
  "zip": "80556"
}


def stringify(num: int) -> str:
    return str(num)

def plus(num1: int, num2: float = 3.5) -> float:
    return num1 + num2

def greet(name: str) -> None:
    return "Hi! " + str

def repeat(message: str, times: int = 2) -> list:
    return [message] * times