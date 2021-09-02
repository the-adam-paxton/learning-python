class Phone:
    # This defines the Attributes
    def __init__(self, brand, price, camera):
        self.brand = brand
        self.price = price
        self.camera = camera

    # This is an example Behaviour
    def call(self, phone_number):
        print(f"{self.brand} is calling calling {phone_number}")

    def photo(self):
        if self.camera == True:
            return "You can take photos"
        else:
            return "No photo ability sadly"

    # What is happening here is that when we call print() on this class, it goes off and looks for the str function,
    # which we have over written here. So this method is called when we use the print() or str() on an object from
    # this class
    def __str__(self) -> str:
        return f"Brand {self.brand} and price {self.price}"

    # dunder repr (cool kids ways of saying 'double under repr') also gives a str representation of the object.
    # __str__ is meant to be more human friendly, whereas __repr__ is supposed to contain info about the object in such
    # a manner that it could be constructed again
    def __repr__(self):
        return f"phone(brand={self.brand}, price={self.price}, camera={self.camera})"


# We are creating two objects, a phone object called iphone and a phone object called samsung, with their respective
# attributes
iphone = Phone("Iphone 7+", 300, False)
samsung = Phone("Samsung S20", 1400, True)

print(iphone.__str__())
print(samsung.__str__())
print(iphone.__repr__())