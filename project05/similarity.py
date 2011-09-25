# similarity metric functions
#
# each function takes two iterable objects, where the values returned by the
# iteration corresponds to the values that should be used for calculating the
# similarity metrics; some functions take the values into account, while
# others do not

import unittest

from statistics import *

# the minkowski distance, where r is the exponent to use
def minkowski_distance(a, b, r):
   a = list(a)
   b = list(b)

   s = sum([pow(abs(i - j), r) for i, j in zip(a, b)])

   return pow(s, 1.0/r)

# returns a similarity - 0.0 = not similar, 1.0 = equal
def euclidean_similarity(a, b):
   return 1.0 / (1.0 + minkowski_distance(a, b, 2))

# returns a similarity - 0.0 = not similar, 1.0 = equal
def simple_matching_similarity(a, b):
   a = list(a)
   b = list(b)
   zipped = zip(a, b)

   match = sum([1 for i, j in zipped if i == j])
   total = len(zipped)

   return float(match) / total

# returns a similarity - 0.0 = not similar, 1.0 = equal
# attributes are converted to booleans
def jacard_similarity(a, b):
   a = list(a)
   b = list(b)
   zipped = zip(a, b)

   match = sum([1 for i, j in zipped if i == j and bool(i) == True])
   total = sum([1 for i, j in zipped if i or j])

   return float(match) / total

# returns a similarity - 0.0 = not similar, 1.0 = equal
def tanimoto_simmilarity(a, b):
   a = list(a)
   b = list(b)

   dotproduct = sum([i * j for i, j in zip(a, b)])

   maga_squared = sum([pow(i, 2) for i in a])
   magb_squared = sum([pow(i, 2) for i in b])

   return float(dotproduct) / (maga_squared + magb_squared - dotproduct)

# returns a similarity - 0.0 = not similar, 1.0 = equal
def cosine_similarity(a, b):
   a = list(a)
   b = list(b)
   zipped = zip(a, b)

   dotproduct = sum([i * j for i, j in zipped])
   maga = minkowski_distance([0] * len(a), a, 2)
   magb = minkowski_distance([0] * len(b), b, 2)

   return float(dotproduct) / (maga * magb)

# returns a correlation - -1.0 = negatively correlated, 1.0 = positively
# correlated, 0.0 = not correlated
def pearson_correlation(a, b):
   a = list(a)
   b = list(b)

   return covariance(a, b) / \
          (sample_standard_deviation(a) * sample_standard_deviation(b))

#
# Test functions
#
class TestSimilarityFunctions(unittest.TestCase):
   def test_euclidean_distance(self):
      a = (0, 0)
      b = (3, 4)
      assert minkowski_distance(a, b, 2) == 5
      assert euclidean_similarity(a, b) == 1.0 / 6

   def test_simple_matching_similarity(self):
      a = (0, 0, 1, 1)
      b = (0, 1, 0, 1)
      assert simple_matching_similarity(a, b) == 1.0 / 2.0

   def test_jacard(self):
      a = (0, 0, 1, 1)
      b = (0, 1, 0, 1)
      assert jacard_similarity(a, b) == 1.0 / 3.0

   def test_tanimoto(self):
      a = (0, 0, 1, 1)
      b = (0, 1, 0, 1)
      assert tanimoto_simmilarity(a, b) == 1.0 / 3.0

   def test_cosine(self):
      a = (3, 2, 0, 5, 0, 0, 0, 2, 0, 0)
      b = (1, 0, 0, 0, 0, 0, 0, 1, 0, 2)
      assert abs(cosine_similarity(a, b) - 0.31497) < 0.001

   def test_pearson(self):
      a = (-3,  6, 0,  3, -6)
      b = ( 1, -2, 0, -1,  2)
      assert abs(pearson_correlation(a, b) - -1.0) < 0.001

      a = (3, 6, 0, 3, 6)
      b = (1, 2, 0, 1, 2)
      assert abs(pearson_correlation(a, b) - 1.0) < 0.001

if __name__ == "__main__":
   unittest.main()
