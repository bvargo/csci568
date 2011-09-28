# a class that represents an iris
# the comparison values stored in cluster_attributes are used for comparison
# this is accomplished by making this object iterable
class Iris(object):
   sepal_length = 0
   sepal_width  = 0
   petal_length = 0
   petal_width  = 0
   name = ""

   cluster_attributes = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
   current_attribute = 0

   def __init__(self,               \
                sepal_length = 0,   \
                sepal_width  = 0,   \
                petal_length = 0,   \
                petal_width  = 0,   \
                name = ""):
      self.sepal_length = sepal_length
      self.sepal_width  = sepal_width
      self.petal_length = petal_length
      self.petal_width  = petal_width
      self.name = name

   def __repr__(self):
      return "%s: %f %f %f %f" % (self.name,
                                  self.sepal_length,
                                  self.sepal_width,
                                  self.petal_length,
                                  self.petal_width)

   def __iter__(self):
      self.current_attribute = 0
      return self

   def __len__(self):
      return len(self.cluster_attributes)

   def __eq__(self, other):
      return self.sepal_length == other.sepal_length and \
             self.sepal_width == other.sepal_width   and \
             self.petal_length == other.petal_length and \
             self.petal_width == other.petal_width   and \
             self.name == other.name

   def __hash__(self):
      value = 0
      value = 31 * value + self.sepal_length
      value = 31 * value + self.sepal_width
      value = 31 * value + self.petal_length
      value = 31 * value + self.petal_width
      value = 31 * value + hash(self.name)
      return value

   def next(self):
      self.current_attribute += 1
      if self.current_attribute > len(self.cluster_attributes):
         raise StopIteration
      else:
         attribute = self.cluster_attributes[self.current_attribute - 1]
         return getattr(self, attribute)
