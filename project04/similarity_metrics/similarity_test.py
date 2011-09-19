#!/usr/bin/env python

from similarity import *

def test_euclidean_distance():
   a = (0, 0)
   b = (3, 4)
   assert minkowski_distance(a, b, 2) == 5
   assert euclidean_similarity(a, b) == 1.0 / 6

def test_simple_matching_coefficient():
   a = (0, 0, 1, 1)
   b = (0, 1, 0, 1)
   assert simple_matching_coefficient(a, b) == 1.0 / 2.0

def test_jacard():
   a = (0, 0, 1, 1)
   b = (0, 1, 0, 1)
   assert jacard_similarity(a, b) == 1.0 / 3.0

def test_tanimoto():
   a = (0, 0, 1, 1)
   b = (0, 1, 0, 1)
   assert tanimoto_simmilarity(a, b) == 1.0 / 3.0

def test_cosine():
   a = (3, 2, 0, 5, 0, 0, 0, 2, 0, 0)
   b = (1, 0, 0, 0, 0, 0, 0, 1, 0, 2)
   assert abs(cosine_similarity(a, b) - 0.31497) < 0.001

if __name__ == "__main__":
   for test in [test_euclidean_distance, test_simple_matching_coefficient, test_jacard, test_tanimoto, test_cosine]:
      print "Running", test
      test()
      print "PASSED"
