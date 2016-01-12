def process_user_input():
    """Asks the user for restaurant and rating until user quits"""

    user_data = {}

    while True:
        user_prompt = raw_input("Would you like to add a restaurant rating? y/n ")
        if user_prompt.lower() == "n":
            return user_data
            break
        elif user_prompt.lower() == "y":
            user_input_restaurant = raw_input("Please enter a restaurant: ")
            user_input_score = raw_input("Please enter a restarant score: ")
            user_data[user_input_restaurant] = user_input_score
        else:
            print "This is not a valid answer."


def alphabetize_restaurant_ratings(filename):
    """Returns each restaurant and its rating, in alphabetical order

    after processing user_input
    """

    restaurant_log = open(filename)

    restaurants = {}

    for line in restaurant_log:
        data = line.rstrip().split(":")
        restaurants[data[0]] = data[1]

    alphabetized_restaurants = sorted(restaurants.items(), key=lambda row: row[0])

    for restaurant in alphabetized_restaurants:
        print "%s is rated at %s." % (restaurant[0], restaurant[1])


alphabetize_restaurant_ratings("scores.txt")
