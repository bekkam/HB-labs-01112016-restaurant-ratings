
def update_random_restaurant(filename):
    """Updates random restaurant with new rating from user"""

    raw_data = {}

    name = raw_input("Hello! What is your name?")
    print "Hi %s" % (name)

    restaurant_log = open(filename)
    for line in restaurant_log:
            data = line.rstrip().split(":")
            raw_data[data[0]] = data[1]

    while True:
        #get_restaurant_name = 
        # dictionary.keys() use random() to select index of the restaurant 
        



update_random_restaurant("scores.txt")
