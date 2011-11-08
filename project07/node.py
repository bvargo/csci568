# a single node in the neural network

import math

from arc import Arc

class Node(object):
   # lists of arcs
   parents = []
   children = []

   # the initial value of the node
   initial_value = 0

   # if parents and/or children are specified, it is assumed that hte arcs are
   # configured by an external function
   def __init__(self, initial_value = 0, parents = None, children = None):
      self.initial_value = initial_value

      self.parents = parents
      if self.parents is None:
         self.parents = []

      self.children = children
      if self.children is None:
         self.children = []

   def add_parent(self, parent, weight):
      a = Arc(parent, self, weight)
      self.parents.append(a)
      parent.children.append(a)

   def add_child(self, child, weight):
      a = Arc(self, child, weight)
      self.children.append(a)
      child.parents.append(a)

   def value(self):
      current_sum = self.initial_value

      for parent in self.parents:
         current_sum += parent.parent.value() * parent.weight

      return math.tanh(current_sum)

   def __repr__(self):
      return "N(%f)" % (self.value())
