# similarity metric functions
#
# each function takes two iterable objects, where the values returned by the
# iteration corresponds to the values that should be used for calculating the
# similarity metrics; some functions take the values into account, while
# others do not

# the minkowski distance, where r is the exponent to use
def minkowski_distance(a, b, r):
   a = list(a)
   b = list(b)
   s = sum([pow(abs(i - j), r) for i, j in zip(a, b)])
   return pow(s, 1.0/r)

def euclidean_similarity(a, b):
   return 1.0 / (1.0 + minkowski_distance(a, b, 2))
