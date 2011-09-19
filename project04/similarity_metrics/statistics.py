# statistics functions

import math

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
