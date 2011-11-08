#!/usr/bin/env python

import math
import random

from node import Node
from arc import Arc

# approximation of slope of tanh, provided by CI
def dtanh(x):
   return 1.0 - x * x

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

# back propogation on the network with the specified output values and the
# learning rage
def backpropogate(network, target_values, N=0.5):
   output_delta = [0.0] * len(network[-1])
   hidden_delta = [0.0] * len(network[-2])

   # calculate delta values for the output layer
   for i, onode in enumerate(network[-1]):
      # the node's value
      value = onode.value()

      # error in the value
      error = target_values[i] - value

      # calculate the delta based on the error
      output_delta[i] = dtanh(value) * error

   # calculate delta values for the hidden layer
   for i, hnode in enumerate(network[1]):
      error = 0.0
      for k, parent_arc in enumerate(hnode.parents):
         error += output_delta[k] * parent_arc.weight
      hidden_delta[i] = dtanh(hnode.value()) * error

   # update output weights
   for i, hnode in enumerate(network[1]):
      for j, child_arc in enumerate(hnode.children):
         change = output_delta[j] * hnode.value()
         child_arc.weight += N * change

   # update input weights
   for i, inode in enumerate(network[0]):
      for j, hidden_arc in enumerate(inode.children):
         change = hidden_delta[j] * inode.value()
         hidden_arc.weight += N * change

if __name__ == "__main__":
   # construct a network with 3 input nodes, 2 hidden nodes, and 3 output
   # nodes
   # the initial values should be as listed in the second argument
   n = construct_network([3,2,3], [1.0, 0.25, -0.5])
   print "Before training:"
   print n
   print

   for i in range(0, 100):
      backpropogate(n, [1.0, -1.0, 0.0])

   print "After 100 back propogations"
   print n
