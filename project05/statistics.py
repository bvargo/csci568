# statistics functions

import math
import unittest

# calculates the covariance
# a and b must be of the same length
def covariance(a, b):
   n = len(a)
   abar = average(a)
   bbar = average(b)
   return 1.0 / (n - 1) * sum([(i - abar) * (j - bbar) for i, j in zip(a, b)])

def sample_standard_deviation(a):
   n = len(a)
   abar = average(a)
   return math.sqrt(1.0 / (n - 1) * sum([pow(i - abar, 2) for i in a]))

def average(a):
   return float(sum(a)) / len(a)

#
# Test functions
#
class TestStatisticsFunctions(unittest.TestCase):
   def test_covariance(self):
      a = [1, 1, 1, 1, 1]
      b = [1, 1, 1, 1, 1]
      assert covariance(a, b) == 0

      a = [1, 2, 3, 4, 5]
      b = [1, 2, 3, 4, 5]
      assert covariance(a, b) == 2.5

   def test_sample_standard_deviation(self):
      pass

   def test_average(self):
      a = [1, 2, 3, 4, 5]
      assert average(a) == 3

if __name__ == "__main__":
   unittest.main()
