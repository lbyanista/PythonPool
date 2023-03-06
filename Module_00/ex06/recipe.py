# Part 1: Nested Dictionaries
cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}

def print_recipe_names():
    print("Recipes: ")
    for recipe_name in cookbook:
        print(recipe_name)

def print_recipe(recipe_name):
    if recipe_name in cookbook:
        recipe = cookbook[recipe_name]
        print("Recipe for ", recipe_name + ": ")
        print("Ingredients list: ", ", ".join(recipe["ingredients"]))
        print("To be eaten for ", recipe["meal"] + ".")
        print("Takes " + str(recipe["prep_time"]) + " minutes of cooking.")
    else:
        print("Recipe not found.")

def delete_recipe(recipe_name):
    if recipe_name in cookbook:
        del cookbook[recipe_name]
        print(recipe_name + " has been deleted.")
    else:
        print("Recipe not found.")

def add_recipe():
    recipe_name = input("Enter recipe name: ")
    if recipe_name in cookbook:
        print("Recipe already exists.")
    else:
        ingredients = input("Ingredients (comma-separated): ").split(",")
        meal = input("Enter Meal type : ")
        prep_time = int(input("Enter Preparation time in minutes: "))
        cookbook[recipe_name] = {
            "ingredients": ingredients,
            "meal": meal,
            "prep_time": prep_time
        }
        print(recipe_name + " has been added.")
    
def print_cookbook():
    print("Cookbook: ")
    for recipe_name in cookbook:
        print_recipe(recipe_name)

def main():
    print("Welcome to the Python Cookbook !")
    while True:
        print("List of available options: ")
        print(" 1: Add a recipe")
        print(" 2: Delete a recipe")
        print(" 3: Print a recipe")
        print(" 4: Print the cookbook")
        print(" 5: Quit")
        choice = input("Please select an option: ")
        if choice == "1":
            add_recipe()
        elif choice == "2":
            recipe_name = input("Enter a recipe name to delete: ")
            if recipe_name in cookbook:
                delete_recipe(recipe_name)
            else:
                print("Recipe not found.")
        elif choice == "3":
            recipe_name = input("Enter a recipe name to print: ")
            if recipe_name in cookbook:
                print_recipe(recipe_name)
            else:
                print("Recipe not found.")
        elif choice == "4":
            print_cookbook()
        elif choice == "5":
            print("Cookbook closed. Goodbye !")
            break
        else:
            print("Sorry, this option does not exist.")

if __name__ == "__main__":
    main()