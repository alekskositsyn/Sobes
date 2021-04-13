class ItemDiscount:
    def __init__(self, name, price: int):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        self._price = new_price


class ItemDiscountReport1(ItemDiscount):
    def __init__(self, name, price, discount: int):
        super().__init__(name, price)
        self.discount = discount

    def get_info(self):
        return self.get_name()

    def get_parent_data(self):
        print(f"Название продукта: {self.get_name()} Цена продукта: {self.get_price()}$ со скидкой:{self.calc()}")

    def calc(self):
        discount_price = self.get_price() - self.get_price() * self.discount / 100
        return discount_price


class ItemDiscountReport2(ItemDiscount):

    def get_info(self):
        return self.get_price()


product1 = ItemDiscountReport1('GalaxyS21', 300, 10)
product2 = ItemDiscountReport2('GalaxyS20', 250)

print(product1.get_info())
print(product2.get_info())

for item in [product1, product2]:
    print(item.get_info())


def handler(obj):
    print(obj.get_info())


handler(product1)
handler(product2)
