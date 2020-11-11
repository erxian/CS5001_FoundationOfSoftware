'''
Zengping
CS 5001 Fall 2020

This program get inputs from user about whether read
or write recipes. If the user intend to write a recipe,
then prompts the user to enter the ingredients, directions,
time and recipe names. If the user intend to read a recipe,
then prompts the user to enter the recipe name,and print
the content.
'''


MENU = ("1", "2", "3")
SUFFIX = ".txt"


def convert_name(name):
    '''
    Function -- convert_name
        convert recipe name to standard format, convert the
        recipe name to lowercase, remove any leading or trailing
        whitespace, convert any other white space to underscores,
        then remove any remaining non-alphanumeric characters and
        add ".txt"
    Parameters:
        name -- a string
    Returns:
        a string, with the standart format
    '''
    name = name.lower().strip().replace(" ", "_")
    for char in name:
        if char != "_":
            if not char.isalpha() and not char.isdigit():
                name = name.replace(char, "")
    return name + SUFFIX


def write_recipe(r, f, i, t, d):
    '''
    Function -- write_recipe
        use the filename to create a file, save recipe name,
        ingredients, time, and direction to the file
    Parameters:
        r -- recipe name
        f -- filename
        i -- ingredients
        t -- time
        d -- direction
    Returns: no returns
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
    USER_PROMPT = "MENU: 1 - Save a new recipe, 2 - Read a \
recipe, 3 - Quit "
    INGREDIENT_PROMPT = "Enter the ingredients on one line. \
Separate each ingredient with a comma. "
    DIRECTION_PROMPT = "Enter the directions (1 paragraph only): "
    TIME_PROMPT = "Enter the time needed in minutes: "
    NAME_PROMPT = "Enter a name for the recipe: "
    Quit = MENU[2]
    user_in = input(USER_PROMPT)
    while user_in != Quit:
        if user_in not in MENU:
            print("Invalid choice.")
        else:
            if user_in == MENU[0]:  # save a new recipe
                validate = False
                # input ingredient
                ingredient = input(INGREDIENT_PROMPT)
                while not validate:
                    ingredients = ingredient.split(",")
                    for i in range(len(ingredients)):
                        ingredients[i] = ingredients[i].strip()
                    for item in ingredients:
                        if len(item) > 0:
                            validate = True
                    if not validate:
                        print("Recipe must have at least one ingredient.")
                        ingredient = input(INGREDIENT_PROMPT)
                # input direction
                direction = input(DIRECTION_PROMPT)
                time_valid = False
                # input time
                time = input(TIME_PROMPT)
                while not time_valid:
                    try:
                        if int(time) < 0:
                            raise Exception
                        else:
                            time_valid = True
                    except Exception:
                        print("Invalid time. Must be an integer \
greater than or equal to 0.")
                        time = input(TIME_PROMPT)
                # input recipe name
                recipe_name = input(NAME_PROMPT)
                converted_name = convert_name(recipe_name)
                filename = ""
                if converted_name == SUFFIX:
                    print("Unable to create the filename.")
                    filename = SUFFIX
                    while filename == SUFFIX:
                        filename = input("Enter a string containing only \
letters, numbers, and spaces ")
                        filename = convert_name(filename)
                else:
                    filename = converted_name
                # create a file and save above info into it
                write_recipe(
                            recipe_name, filename, ingredients,
                            time, direction)
                print("%s recipe saved to %s" % (recipe_name, filename))
            if user_in == MENU[1]:  # read a recipe
                recipe_name = input("Enter the name of the recipe: ")
                filename = convert_name(recipe_name)
                try:
                    file = open(filename, "r")
                    print(file.read())
                    file.close()
                except FileNotFoundError:
                    print("Unable to read", filename)
        user_in = input(USER_PROMPT)


if __name__ == "__main__":
    main()
