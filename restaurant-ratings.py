# your code goes here


# sort by [0]

def alphabetized_restaurant_ratings(filename):
    """Returns each restaurant and its rating, in alphabetical order"""

    restaurant_log = open(filename)

    alphabetized_data = []

    for line in restaurant_log:
        line = line.rstrip()
        data = line.split(":")
        alphabetized_data.append(data)

    #result = alphabetized_data.sort(key= lambda row: row[0])
    result = sorted(alphabetized_data, key= lambda row: row[0])
    print result

 





    #for data[0] in data:



alphabetized_restaurant_ratings("scores.txt")