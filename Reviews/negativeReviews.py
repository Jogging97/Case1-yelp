import numpy as np
import pandas as pd

import Reviews.reviewHelpers as rh
from Reviews import mapping


def main():
    # businesses = pd.read_csv("../Yelp Data Files/CSV Files/business.csv")
    reviews = pd.read_csv("../Yelp Data Files/CSV Files/review.csv")
    # users = pd.read_csv("../Yelp Data Files/CSV Files/user.csv")
    # photos = pd.read_csv("../Yelp Data Files/CSV Files/photo.csv")

    negativeReviews = reviews[reviews["stars"] < 2]
    positiveReviews = reviews[reviews["stars"] > 3]

    cntNegReviews = len(negativeReviews)
    cntPosReviews = len(positiveReviews)

    print("Count of Negative Views: ", cntNegReviews)
    print("Count of Positive Views: ", cntPosReviews)

    negPhrases = wordmap(negativeReviews)

    createMap(negPhrases, "neg")


def getReviewType(userReview):
    print("Hi")


def promptUser():
    userReview = input("Please enter a review: ")


def wordmap(reviewDF):
    reviews_dict = {}

    for bID in reviewDF["business_id"].values:
        try:
            reviews_dict[bID] = reviews_dict[bID] + 1
        except:
            reviews_dict[bID] = 1

    businesses = pd.DataFrame.from_dict(data=reviews_dict, orient="index")

    businesses.reset_index(inplace=True)
    businesses.columns = ['business_id', 'rated']

    return []

def createMap(values, type):
    stdin = values.tobytes()

    job = mapping.ReviewCount()
    job.sandbox(stdin=stdin)

    runner = job.make_runner()

    runner.run()

    f = open(type + "_reviews.csv", "w")

    for line in runner.stream_output():
        # Use the job's specified protocol to read an output key-value pair
        key, value = job.parse_output_line(line)

        s = "%s,%d\n" % (key, value)
        f.write(s)