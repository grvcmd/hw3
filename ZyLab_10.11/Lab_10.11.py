class FoodItem:
    def __init__(self, name, fat, carbs, protein):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def __init__(self, name = None, fat = 0.0, carbs = 0.0, protein = 0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein


    def print_example_nutrition_info(self):
        print('Nutritional information per serving of None:')
        print('   Fat: 0.00 g')
        print('   Carbohydrates: 0.00 g')
        print('   Protein: 0.00 g')

    def get_calories(self):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * servings
        return calories

    def print_nutrition_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))



food_name = str(input())
amount_fat = float(input())
amount_carbs = float(input())
amount_protein = float(input())

servings = float(input())

lunch = FoodItem(food_name, amount_fat, amount_carbs, amount_protein)

lunch.print_example_nutrition_info()
print('Number of calories for {:.2f} serving(s): 0.00\n'.format(servings))
lunch.print_nutrition_info()
print('Number of calories for {:.2f} serving(s): {:.2f}'.format(servings, lunch.get_calories()))