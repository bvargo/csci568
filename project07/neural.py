#!/usr/bin/env python

import random
import math

from node import Node
from arc import Arc

# sizes is an array of integers, indicating the size of each layer
# input_values is a list of input values for the first layer of the network;
# if None, then the initial values are not set
# returns an array of layers, where index 0 is the start and index -1 is the
# end
# each layer is itself an array of nodes
def construct_network(sizes, input_values = None):
   network = []
   for layer_size in sizes:
      current_layer = []

      # create the layer
      for node in range(0, layer_size):
         current_layer.append(Node())

      # connect to the previous layer
      if len(network):
         for current_node in current_layer:
            for parent_node in network[-1]:
               random_weight = random.random() * 2 - 1
               current_node.add_parent(parent_node, random_weight)

      # add the current layer to the network
      network.append(current_layer)

   # set the input values
   if input_values:
      set_input_values(network, input_values)

   # end of network creation - return the result
   return network

# sets the input values on the network to input_values
def set_input_values(network, input_values):
   for node, value in zip(network[0], input_values):
      node.initial_value = value

if __name__ == "__main__":
   n = construct_network([3,2,3], [1.0, 0.25, -0.5])
   print n
