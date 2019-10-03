import numpy as np
import pandas as pd

import Reviews.reviewHelpers as rh

businesses = pd.read_csv("../Yelp Data Files/CSV Files/business.csv")
reviews = pd.read_csv("../Yelp Data Files/CSV Files/review.csv")
users = pd.read_csv("../Yelp Data Files/CSV Files/user.csv")
photos = pd.read_csv("../Yelp Data Files/CSV Files/photo.csv")

negativeReviews = reviews[reviews["stars"] < 2]
positiveReviews = reviews[reviews["stars"] >= 3]

cntNegReviews = len(negativeReviews)
cntPosReviews = len(positiveReviews)

print("Count of Negative Views: ", cntNegReviews)
print("Count of Positive Views: ", cntPosReviews)

neg_reviews_dict = {}

for bID in negativeReviews["business_id"].values:
    try:
        neg_reviews_dict[bID] = neg_reviews_dict[bID] + 1
    except:
        neg_reviews_dict[bID] = 1

negBus = pd.DataFrame.from_dict(data=neg_reviews_dict, orient="index")

negBus.reset_index(inplace=True)
negBus.columns = ['business_id', 'rated']

print(negBus.head(15))

negBus = negBus[negBus['rated'] > 200]

print(negBus.head(15))
# num_business_analysis = 1 # basically this will tell how much computing and diverse our analysis will be
# business_ids=bottom_business_data.sort_values("rated")[::-1][:num_business_analysis].business_id.values
# business_names = bottom_business_data.sort_values("rated")[::-1][:num_business_analysis]["Business name"].values
# # get all the reviews and analyse them
# #business_names
# for i, business_id in enumerate(business_ids):
#     # now extract reviews from reviews data
#     print("Analysing business: ", business_names[i])
#     reviews = reviews.loc[reviews['business_id'] == business_id].text.values
#     most_used_text = rh.count_ngrams(reviews, max_length=3)
#     rh.print_most_frequent(most_used_text, num=10)
