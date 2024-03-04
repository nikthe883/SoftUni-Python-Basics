class Shop:


    def __init__(self, name, type, capacity) -> None:
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}


    @classmethod
    def small_shop(cls, name, type):
            return cls(name, type, 10)
        
    def add_item(self, item):
        if self.capacity - (len(self.items) + 1) > 0:
             
            if item in self.items:
                self.items[item] += 1
            else:
                self.items[item] = 1

            return f"{item} added to the shop"
        return f"Not enough capacity in the shop"
    
    def remove_item(self, item_name, amount):
        if item_name not in self.items:
            return f"Cannot remove {amount} {item_name}"

        if self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount

        if self.items[item_name] <= 0:
            del self.items[item_name]

        return f"{amount} {item_name} removed from the shop"
    def __repr__(self) -> str:
         return f"{self.name} of type {self.type} with capacity {self.capacity}"
    
fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)
