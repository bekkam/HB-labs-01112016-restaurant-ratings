# your code goes here


def alphabetized_restaurant_ratings(filename):
    """Returns each restaurant and its rating, in alphabetical order"""

    restaurant_log = open(filename)

    raw_data = {}

    for line in restaurant_log:
        line = line.rstrip()
        data = line.split(":")
        raw_data[data[0]] = data[1]

    result = sorted(raw_data.items(), key = lambda row: row[0])

    for restaurant in result:
        print "%s is rated at %s." % (restaurant[0], restaurant[1])


alphabetized_restaurant_ratings("scores.txt")