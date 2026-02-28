
class product:
    id = 78
    name = 'Amul'

    def display(self):
        print(f'Product ID {self.id} & Product name {self.name}')

class tyepa(product):
    count = 50
    category = 'butter'

    def display(self):
        print(f'Product ID {self.id} & Product name {self.name} & count is {self.count} of category {self.category}')

class tyepb(product):
    count = 90
    category = 'Milk'

    def display(self):
        print(f'Product ID {self.id} & Product name {self.name} & count is {self.count} of category {self.category}')

class tyepc(product):
    count = 56
    category = 'choco'

    def display(self):
        print(f'Product ID {self.id} & Product name {self.name} & count is {self.count} of category {self.category}')
              



p1 = product()
p1.display()
p2 = tyepa()
p2.display()
p3 = tyepb()
p3.display()
p4 = tyepc()
p4.display()





