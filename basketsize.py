class Basket:
    sole = ["orange", "apple", "mango"]

    def __init__(self, size: int) -> None:
        self.size = size
        self.basket = []

    def add(self, item: str) -> None:
        self.basket.append(item)
        if len(self.basket) > self.size:
            self.basket.pop(0)


flow = Basket(3)
b = ["orange", "apple", "berry"]

print(flow.add("b"))
