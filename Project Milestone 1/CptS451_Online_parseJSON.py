import json

def cleanStr4SQL(s):
    return s.replace("'", "''").replace("\n", " ")

def getAttributes(attributes):
    L = []
    for (attribute, value) in list(attributes.items()):
        if isinstance(value, dict):
            L += getAttributes(value)
        else:
            L.append((attribute, value))
    return L

def parseBusinessData():
    print("Parsing businesses...")
    with open('yelp_business.json', 'r') as f:
        outfile = open('yelp_business.txt', 'w')
        line = f.readline()
        count_line = 0
        while line:
            data = json.loads(line)
            business_id = data['business_id']
            business_str = "'{}','{}','{}','{}','{}',{},{},{},{},{}".format(
                cleanStr4SQL(data['name']),
                cleanStr4SQL(data['address']),
                cleanStr4SQL(data['city']),
                data['state'],
                data['postal_code'],
                data['latitude'],
                data['longitude'],
                data['stars'],
                data['review_count'],
                data['is_open']
            )
            outfile.write(business_str + '\n')
            line = f.readline()
            count_line += 1
    print(count_line)
    outfile.close()
    f.close()

def parseReviewData():
    print("Parsing reviews...")
    with open('yelp_review.json', 'r') as f:
        outfile = open('yelp_review.txt', 'w')
        line = f.readline()
        count_line = 0
        while line:
            data = json.loads(line)
            review_str = "'{}','{}','{}',{},'{}','{}',{},{},{}".format(
                data['review_id'],
                data['user_id'],
                data['business_id'],
                data['stars'],
                data['date'],
                cleanStr4SQL(data['text']),
                data['useful'],
                data['funny'],
                data['cool']
            )
            outfile.write(review_str + '\n')
            line = f.readline()
            count_line += 1
    print(count_line)
    outfile.close()
    f.close()

def parseUserData():
    print("Parsing users...")
    with open('yelp_user.json', 'r') as f:
        outfile = open('yelp_user.txt', 'w')
        line = f.readline()
        count_line = 0
        while line:
            data = json.loads(line)
            user_id = data['user_id']
            user_str = "'{}','{}','{}',{},{},{},{},{},{}".format(
                user_id,
                cleanStr4SQL(data["name"]),
                cleanStr4SQL(data["yelping_since"]),
                data["review_count"],
                data["fans"],
                data["average_stars"],
                data["funny"],
                data["useful"],
                data["cool"]
            )
            outfile.write(user_str + "\n")

            for friend in data["friends"]:
                friend_str = "'{}','{}'\n".format(user_id, friend)
                outfile.write(friend_str)
            line = f.readline()
            count_line += 1
    print(count_line)
    outfile.close()
    f.close()

def parseCheckinData():
    print("Parsing checkins...")
    with open('yelp_checkin.json', 'r') as f:
        outfile = open('yelp_checkin.txt', 'w')
        line = f.readline()
        count_line = 0
        while line:
            data = json.loads(line)
            business_id = data['business_id']
            for dayofweek, time in data['time'].items():
                for hour, count in time.items():
                    checkin_str = "'{}','{}','{}',{}".format(
                        business_id,
                        dayofweek,
                        hour,
                        count
                    )
                    outfile.write(checkin_str + "\n")
            line = f.readline()
            count_line += 1
    print(count_line)
    outfile.close()
    f.close()

parseBusinessData()
parseUserData()
parseCheckinData()
parseReviewData()
