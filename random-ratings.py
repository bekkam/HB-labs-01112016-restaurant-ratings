
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
        

# # your code goes here
# def process_user_input():
#     """Asks the user for restaurant and rating until user quits"""

#     user_data = {}

#     while True:
#         user_prompt = raw_input("Would you like to add a restaurant rating? y/n ")
#         if user_prompt.lower() == "n":
#             return user_data
#             break
#         elif user_prompt.lower() == "y":
#             user_input_restaurant = raw_input("Please enter a restaurant: ")
#             user_input_score = raw_input("Please enter a restarant score: ")
#             user_data[user_input_restaurant] = user_input_score
#         else:
#             print "This is not a valid answer"

update_random_restaurant("scores.txt")
