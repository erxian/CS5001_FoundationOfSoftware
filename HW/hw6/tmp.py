SUFFIX = ".txt"

def convert_name(name):
    '''
    '''
    name = name.lower().strip().replace(" ", "_")
    for char in name:
        #print(char, name)
        if char != "_":
            if not char.isalpha() and not char.isdigit():
                name = name.replace(char, "")
    return name + SUFFIX


def write_recipe(r, f, i, t, d):
    '''
    '''
    recipe_name = r
    filename = f
    ingredients = i
    time = t
    direction = d
    with open(filename, "w") as file:
        file.write(recipe_name + "\n")
        file.write("\n")
        file.write("Ingredients:\n")
        for item in ingredients:
            file.write(item + "\n")
        file.write("\n")
        file.write("Time: %s minutes\n" % time)
        file.write("\n")
        file.write("Directions:\n")
        file.write(direction)


def main():
    #print(convert_name(" aaf * gg"))
    r = "Egg and Soldiers"
    f = "egg_and_soldiers.txt"
    i = ["1 egg", "1 slice of bread", "butter"]
    t = "15"
    d = "Soft boil the egg and remove the top of the shell.\
Toast and butter the bread. Cut the bread into slices."
    write_recipe(r, f, 
    i, t, d)

    # recipe_name = input("Enter a name: ")
    # recipe_name = convert_name(recipe_name)
    # print(recipe_name)
    # filename = ""
    # if recipe_name == SUFFIX:
    #     print("Unable to create the filename")
    #     filename = SUFFIX
    #     while filename == SUFFIX:
    #         filename = input("Enter a string containing only letters, numbers, and spaces ")
    #         filename = convert_name(filename)
    # else:
    #     filename = recipe_name
    # print(filename)
#     INGREDIENT_PROMPT = "Enter the ingredients on one line.\
# Separate each ingredient with a comma. "
#     validate = False
#     ingredient = input(INGREDIENT_PROMPT)
#     while not validate:
#         ingredients = ingredient.split(",")
#         for i in range(len(ingredients)):
#             ingredients[i] = ingredients[i].strip()
#         for item in ingredients:
#             if len(item) > 0:
#                 validate = True
#         if not validate:
#             print("Recipe must have at least one ingredient.")
#             ingredient = input(INGREDIENT_PROMPT)
    # TIME_PROMPT = "Enter the time needed in minutes: "
    # time_valid = False
    # time = input(TIME_PROMPT)
    # while not time_valid:
    #     try:
    #         if int(time) < 0:
    #             raise Exception
    #         else:
    #             time_valid = True
    #     except:
    #         print("Invalid time. Must be an integer greater than or equal to 0.")
    #         time = input(TIME_PROMPT)





if __name__ == "__main__":
    main()