#!/usr/bin/env python

import csv

from iris import Iris
from kmeans import KMeans
from similarity import euclidean_similarity
from plot import create_plot

# imports iris objects from a CSV file
def import_csv(filename="iris.csv"):
   irii = []

   file = open(filename, 'rb')
   reader = csv.reader(file)
   for row in reader:
      if len(row):
         attributes = map(float, row[:4])
         sepal_length, sepal_width, petal_length, petal_width = attributes
         name = row[4]

         iris = Iris(sepal_length, sepal_width, petal_length, petal_width, name)
         irii.append(iris)

   return irii

# the main function
def main():
   # import the data
   irii = import_csv()

   # create and initialize the algorithm
   kmeans = KMeans(3, irii, euclidean_similarity)

   # run the algorithm
   # TODO: stopping condition
   for i in range(0, 50):
      kmeans.next()

   print "SSE Values for each cluster:"
   for cluster_num, sse in enumerate(kmeans.sses()):
      num_members = len(kmeans.clusters[cluster_num])
      print "Cluster %d (%d members): %f" % (cluster_num, num_members, sse)

   print

   # create a plot
   try:
      print "Plotting sepal length vs sepal width."
      print "Colors indicate the cluster, as identified by k-means across all"
      print "attributes. The symbol indicates the 'correct' group, as"
      print "determined by the name of the IRIS. The black + symbols indicate"
      print "the centroids."
      create_plot(kmeans)
   except:
      print "There was a plotting error. Do you have matplotlib installed?"

if __name__ == "__main__":
   main()
