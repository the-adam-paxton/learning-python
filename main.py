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


# We are creating two objects, a phone object called iphone and a phone object called samsung, with their respective
# attributes
iphone = Phone("Iphone 7+", 300, False)
samsung = Phone("Samsung S20", 1400, True)

# Print out the brand and price attributes we have just defined
print(iphone.brand)
print(iphone.price)
# Calling the iphone object we created and the call behaviour with the required parameters
iphone.call("999")

print(samsung.brand)
print(samsung.price)
samsung.call("999")

print(iphone.photo())
