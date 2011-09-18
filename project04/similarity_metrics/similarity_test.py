#!/usr/bin/env python

from similarity import *

def test_euclidean_distance():
   a = (0, 0)
   b = (3, 4)
   assert minkowski_distance(a, b, 2) == 5
   assert euclidean_similarity(a, b) == 1.0 / 6

if __name__ == "__main__":
   for test in [test_euclidean_distance]:
      print "Running", test
      test()
