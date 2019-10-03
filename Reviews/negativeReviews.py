import numpy as np
import pandas as pd

import Reviews.reviewHelpers as rh
from Reviews import mapping


def main():
    yelp_reviews = pd.read_csv("../Yelp Data Files/CSV Files/review.csv")
    # users = pd.read_csv("../Yelp Data Files/CSV Files/user.csv")
    # photos = pd.read_csv("../Yelp Data Files/CSV Files/photo.csv")

    negativeReviews = yelp_reviews[yelp_reviews["stars"] < 2]
    positiveReviews = yelp_reviews[yelp_reviews["stars"] > 3]

    cntNegReviews = len(negativeReviews)
    cntPosReviews = len(positiveReviews)

    print("Count of Negative Views: ", cntNegReviews)
    print("Count of Positive Views: ", cntPosReviews)

    negPhrases = wordmap(yelp_reviews, negativeReviews)

    createMap(negPhrases, "neg")


def getReviewType(userReview):
    print("Hi")


def promptUser():
    userReview = input("Please enter a review: ")


def wordmap(yelp_review, reviewDF):
    reviews_dict = {}

    for bID in reviewDF["business_id"].values:
        try:
            reviews_dict[bID] = reviews_dict[bID] + 1
        except:
            reviews_dict[bID] = 1

    businesses = pd.DataFrame.from_dict(data=reviews_dict, orient="index")

    businesses.reset_index(inplace=True)
    businesses.columns = ['business_id', 'rated']

    yelp_businesses = pd.read_csv("../Yelp Data Files/CSV Files/business.csv")

    top_count = 20
    right = pd.DataFrame(yelp_businesses[['business_id', "name", "categories"]].values,
                         columns=['business_id', "Business name", "categories"])

    businessData = pd.merge(businesses, right=right, how="inner", on='business_id')
    numBusAnal = 1

    bIDs = businessData.sort_values("rated")[::-1][:numBusAnal].business_id.values

    returnVal = []

    for i, business_id in enumerate(bIDs):
        # now extract reviews from reviews data
        reviews = yelp_review.loc[yelp_review['business_id'] == business_id].text.values
        most_used_text = rh.count_ngrams(reviews, max_length=2)

        for i in sorted(most_used_text):
            for gram, count in most_used_text[i].most_common(50):
                returnVal.append('{0}: {1}'.format(' '.join(gram), count))

    return returnVal


def createMap(values, type):
    stdin = values.tobytes() # Error: 'list' object has no attribute 'tobytes'. Need to fix the return of wordmap()

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


if __name__ == "__main__":
    main()
