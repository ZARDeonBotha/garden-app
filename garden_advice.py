def get_season() -> str:
    """
    Gets a season from the user input. This function displays a menu
    of available seasons and prompts the user to select one by entering a
    corresponding number.

    Returns
    -------
    str
        The selected season as a lowercase string.
    """
    valid_seasons = ['summer', 'winter', 'spring', 'autumn']
    while True:
        try:
            print("Choose a season:")
            for idx, season in enumerate(valid_seasons, 1):
                print(f"{idx}. {season.capitalize()}")
            choice = input(
                "Enter the number corresponding to the season: ").strip()
            if (not choice.isdigit()
                or not (1 <= int(choice) <= len(valid_seasons))):
                raise ValueError("Invalid selection. Please enter a number"
                                 " from the menu.")
            return valid_seasons[int(choice) - 1]
        except ValueError as e:
            print(e)

def get_plant_type():
    """
    This function allows the user to select a plant type from a
    pre-defined list of valid plant types. It prompts the user with a menu
    of options, validates the input,
    and returns the selected plant type.

    Args:
        None

    Returns:
        str: The selected plant type from the list of valid options.

    Raises:
        ValueError: If the user's input is not a valid number
        corresponding to a plant type in the list. This includes the case
        where the input is not a number or
        when the number is outside the range of valid options.

    """
    valid_plant_types = ['flower', 'vegetable', 'herb']
    while True:
        try:
            print("Choose a plant type:")
            for idx, plant in enumerate(valid_plant_types, 1):
                print(f"{idx}. {plant.capitalize()}")
            choice = input("Enter the number corresponding to the "
                           "plant type: ").strip()
            if (not choice.isdigit()
                or not (1 <= int(choice) <= len(valid_plant_types))):
                raise ValueError("Invalid selection. Please enter a "
                                 "number from the menu.")
            return valid_plant_types[int(choice) - 1]
        except ValueError as e:
            print(e)

def main():
    # Get user selections
    season = get_season()
    plant_type = get_plant_type()

    # Variable to hold gardening advice
    advice = ""

    # Determine advice based on the season
    if season == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"

    # Determine advice based on the plant type
    if plant_type == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."

    # Print the generated advice
    print("\nGardening Advice:")
    print(advice)

if __name__ == "__main__":
    main()
