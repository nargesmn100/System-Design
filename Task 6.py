class CoffeMaker():
    def __init__(self, drink: str):
        self.drink = drink
        self.water_level = 1000
        self.coffee_bean_level = 500

    def ingredient_refill(self, what_to_refill: str, amount_to_refill: int):
        if  what_to_refill == "water":
            self.water_level += amount_to_refill
        if  what_to_refill == "coffe_bean":
            self.coffe_bean_level += amount_to_refill

    def ingredient_indicator(self):
        if self.water_level < 200:
            self.ingredient_refill("water", 1000)
        if self.coffee_bean_level < 100:
            self.ingredient_refill("coffe_bean", 400)
        return f"All good"

    def drink_maker(self):
        drink_types = {
            "coffee" : {"needed_water": 98, "needed_coffee_beans": 54},
            "latte" : {"needed_water": 59, "needed_coffee_beans": 20},
        }

        if self.drink not in drink_types:
            return f"The requested drink is invalid."
        # Now we need to make sure that we have all the ingredients we need before making the drink
        drnk = drink_types[self.drink]
        if self.ingredient_indicator() == "All good":
            self.coffee_bean_level -= drnk["needed_coffee_beans"]
            self.water_level -= drnk["needed_water"]
            print(f"Drink Made!")

    def status(self):
        """
        Displays the current resource levels.
        """
        print(f"Water: {self.water_level}ml, Coffee Beans: {self.coffee_bean_level}g")


order = CoffeMaker("coffee")
order.drink_maker()
order.status()