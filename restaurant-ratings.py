# your code goes here
def process_user_input():
    """Asks the user for restaurant and rating untill user quits"""
    user_data = {}

    while True:
        user_prompt = raw_input("Would you like to add a restaurant rating? y/n")
        if user_prompt.lower() == "n":
            return user_data
            break
        elif user_prompt.lower() == "y":
            user_input_restaurant = raw_input("Please enter a restaurant")
            user_input_score = raw_input("Please enter a restarant score")
            user_data[user_input_restaurant] = user_input_score
        else:
            print "This is not a valid answer"


def alphabetize_restaurant_ratings(filename):
    """Returns each restaurant and its rating, in alphabetical order

        after processing user input.
    """

    raw_data = process_user_input()

    restaurant_log = open(filename)

    for line in restaurant_log:
        data = line.rstrip().split(":")
        raw_data[data[0]] = data[1]

    result = sorted(raw_data.items(), key = lambda row: row[0])

    for restaurant in result:
        print "%s is rated at %s." % (restaurant[0], restaurant[1])


alphabetize_restaurant_ratings("scores.txt")


