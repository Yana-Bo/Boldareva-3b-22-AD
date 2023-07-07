class Card:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def decrease_quantity(self, summ1):
        if summ1 > 0:
            if self.quantity >= summ1:
                self.quantity -= summ1
                print(f"Кол-во товара: {self.quantity} кг")
            else:
                print(f"Товара меньше {summ1} кг")
                print(f"Кол-во товара в кг: {self.quantity}")
        else:
            print("Количество товара не может быть отрицательным")

    def change_price(self, summ1):
        if self.price >= -summ1:
            self.price += summ1
            print(f"Стоимость товара: {self.price} рублей за кг")
        else:
            print("Стоимость товара не может быть отрицательной")
            print(f"Стоимость товара за кг: {self.price}")


p1 = Card("Черешня", 50, 400)
p1.decrease_quantity(70)
p1.change_price(600)