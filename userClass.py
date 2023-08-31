class User:
    
    DEFAULT_MONEY = 0

    def __init__(self, name: str, age: int, password: str):
        self.name = name
        self.age = age
        self.password = password

    def hello_world(self):
        print(f"Welcome, {self.name}!\nWhat you need do today?")