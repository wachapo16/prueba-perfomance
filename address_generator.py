import random

class AddressGenerator:
    @staticmethod
    def generate_random_address():
        streets = ["Cl", "Cra", "Av", "Cll"]
        street = random.choice(streets)
        number = random.randint(1, 100)
        return f"{street} {number} # {random.randint(1, 100)}"
