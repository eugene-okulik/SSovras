class Flowers:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Rose(Flowers):
    kind = 'Rose'

    def __init__(self, name, color, life_time, price, area):
        super().__init__(name, color)
        self.life_time = life_time
        self.price = price
        self.area = area


class Gvozdika(Flowers):
    kind = 'Gvozdika'

    def __init__(self, name, color, life_time, price, area):
        super().__init__(name, color)
        self.life_time = life_time
        self.price = price
        self.area = area


class Pion(Flowers):
    kind = 'Pion'

    def __init__(self, name, color, life_time, price, area):
        super().__init__(name, color)
        self.life_time = life_time
        self.price = price
        self.area = area


class Bouquet:
    bouquet_price = int
    flowers = []

    def __init__(self, name):
        self.name = name
        self.price = self.total_price()

    def adding_flowers(self, flower):
        self.flowers.append(flower)

    def total_price(self):
        cost = 0
        for i in range(len(self.flowers)):
            cost += self.flowers[i].price
            i += 1
        return cost

    def average_life_time(self):
        average_life_time = 0
        flowers_count = len(self.flowers)
        for i in range(len(self.flowers)):
            average_life_time += self.flowers[i].life_time
            i += 1
        return round(average_life_time / flowers_count, 1)

    def sort_by_color(self):
        return sorted(self.flowers, key=lambda flowers: flowers.color)

    def sort_by_life_time(self):
        return sorted(self.flowers, key=lambda flowers: flowers.life_time)

    def sort_by_price(self):
        return sorted(self.flowers, key=lambda flowers: flowers.price)

    def find_by_name(self, word):
        for i in range(len(self.flowers)):
            return self.flowers[i].name == word


fl_1 = Rose('Red_rose', 'Red', 1, 11, 'Europe')
fl_2 = Rose('Blue_rose', 'Blue', 2, 14, 'Asia')
fl_3 = Rose('White_rose', 'White', 3, 13, 'America')
fl_4 = Pion('Cool_pione', 'Pink', 12, 23, 'Europe')
fl_5 = Pion('Rare_pione', 'Black', 5, 9, 'Australia')
fl_6 = Pion('Cool_pione', 'Yellow', 12, 23, 'Asia')
fl_7 = Gvozdika('Red_gvozdika', 'Red', 12, 23, 'Europe')
fl_8 = Gvozdika('White_gvozdika', 'White', 4, 17, 'Australia')
fl_9 = Gvozdika('Pink_pione', 'Pink', 6, 22, 'Asia')

b_1 = Bouquet('First_bouquet')
b_1.adding_flowers(fl_1)
b_1.adding_flowers(fl_2)
b_1.adding_flowers(fl_3)

b_2 = Bouquet('Second_bouquet')
b_2.adding_flowers(fl_5)
b_2.adding_flowers(fl_3)
b_2.adding_flowers(fl_9)

print(b_1.flowers)  # List with flowers objects
print(b_1.total_price())  # Price for the bouquet
print(b_1.average_life_time())  # Average time of bouquet's life
print(b_1.sort_by_color())  # Objects sorted by color
print(b_1.sort_by_life_time())  # Objects sorted by life_time
print(b_1.sort_by_price())  # Objects sorted by price
print(b_1.find_by_name('Red_rose'))  # Find flower in the bouquet by the flower name
