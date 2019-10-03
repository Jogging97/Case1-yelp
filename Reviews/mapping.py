from mrjob.job import MRJob

class ReviewCount(MRJob):
    """
    Count the phrases based on each key-value pair
    """

    """ Create a Key-Value Pair"""
    def mapper(self, key, value):
        yield value.split(": ")[0], int(value.split(": ")[1])

    def reducer(self, key, values):
        yield key, sum(values)
