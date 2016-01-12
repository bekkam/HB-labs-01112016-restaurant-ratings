# your code goes here


def alphabetize_restaurant_ratings(filename):
    """Returns each restaurant and its rating, in alphabetical order"""

    # while True:
    #     user_prompt = raw_input("Would you like to add a restaurant rating?")
    #        if 

    # user_input_restaurant = raw_input("Please enter a restaurant")
    # user_input_score = raw_input("Please enter a restarant score")

    restaurant_log = open(filename)

    raw_data = {}

    for line in restaurant_log:
        data = line.rstrip().split(":")
        raw_data[data[0]] = data[1]

    result = sorted(raw_data.items(), key = lambda row: row[0])

    for restaurant in result:
        print "%s is rated at %s." % (restaurant[0], restaurant[1])


alphabetized_restaurant_ratings("scores.txt")


