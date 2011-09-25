# runs k-means on arbitrary objects using the specified number of clusters (k)
# and the given similarity function

import sys
import random

class KMeans(object):
   # the number of clusters to use
   k = 0

   # the objects over which k-means should be run
   objects = []

   # the current centroids
   centroids = []

   # the current clusters
   clusters = []

   # the (min, max) pairs for each attribute
   ranges = []

   # similarity function for two objects
   similarity = None

   # initialize k-means for the set of list of iterable objects, a number of
   # clusters(k), and a similarity function that compares a to b
   def __init__(self, k, objects, similarity):
      self.k = k
      self.objects = objects
      self.similarity = similarity

      self.init_attribute_ranges()
      self.init_centroids()

   # initializes the attribute ranges
   def init_attribute_ranges(self):
      first = True
      self.ranges =[]

      # loop over each object and check for minimum or maximum values
      for o in self.objects:
         # first time initialization - use length to setup list of 2-lists
         if first:
            for i in range(0, len(o)):
               self.ranges.append([None, None])
            first = False

         # check for minimum or maximum values
         for i, attribute in enumerate(o):
            if self.ranges[i][0] is None or attribute < self.ranges[i][0]:
               self.ranges[i][0] = attribute
            elif self.ranges[i][1] is None or attribute > self.ranges[i][1]:
               self.ranges[i][1] = attribute

   # initialize centroids
   def init_centroids(self):
      self.centroids = []
      for i in range(0, self.k):
         self.centroids.append(self.generate_random_centroid())

   # generates a random centroid between the min and max values for each
   # attribute
   def generate_random_centroid(self):
      centroid = []
      for r in self.ranges:
         centroid.append(random.uniform(r[0], r[1]))
      return tuple(centroid)

   # next iteration of k-means
   def next(self):
      # clear old clusters
      self.clusters = [[] for i in range(0, len(self.centroids))]

      # associate each object with a centroid
      for o in self.objects:
         max_similarity = 0
         max_centroid = None
         max_centroid_index = 0

         # find the closest centroid
         for i, c in enumerate(self.centroids):
            s = self.similarity(o, c)
            if max_centroid is None or s > max_similarity:
               max_similarity = s
               max_centroid = c
               max_centroid_index = i

         # assign the object to the cluster associated with the closest
         # centroid
         self.clusters[max_centroid_index].append(o)

      # clear the old centroids
      self.centroids = [[]] * len(self.clusters)

      # move each centroid to the middle of each cluster
      for i, c in enumerate(self.centroids):
         self.centroids[i] = self.calculate_centroid(self.clusters[i])

   # calculates the centroid of the cluster
   # if the cluster is empty, a new random centroid is made
   def calculate_centroid(self, cluster):
      centroid = []

      # check for an empty cluster
      if len(cluster) == 0:
         return self.generate_random_centroid()

      # for each attribute number
      for i in range(0, len(cluster[0])):
         # calculate the average value
         s = sum([list(o)[i] for o in cluster])
         n = len(cluster)
         centroid.append(float(s) / n)

      return centroid
