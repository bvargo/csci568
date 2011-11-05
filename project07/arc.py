# links two nodes together

class Arc(object):
   parent = None
   child = None
   weight = 0

   def __init__(self, parent, child, weight):
      self.parent = parent
      self.child = child
      self.weight = weight

   def __repr__(self):
      return "A(%f)" % (self.weight)
