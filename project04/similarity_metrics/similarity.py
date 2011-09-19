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

# returns a similarity - 0.0 = not similar, 1.0 = equal
def euclidean_similarity(a, b):
   return 1.0 / (1.0 + minkowski_distance(a, b, 2))

# returns a similarity - 0.0 = not similar, 1.0 = equal
def simple_matching_coefficient(a, b):
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
