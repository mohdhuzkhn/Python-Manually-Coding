class vehicle:
    def __init__(self , model , rpm):
        self.model = model
        self.rpm = rpm
        print("Hey I run automatically")

    def show(self):
        print(f"Type: {self.model}, RPM: {self.rpm}")


car1 = vehicle("Sedan", 2000)
car1.show()
