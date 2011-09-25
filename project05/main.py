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

   # create a plot
   create_plot(kmeans)

if __name__ == "__main__":
   main()
