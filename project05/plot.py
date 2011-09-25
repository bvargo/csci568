# creates a plot of the k-means data against the first two cluster attributes
# the color indicates the cluster, as produced by the algorithm
# the symbols indicate the "real" clustering based on the name of the iris
# NOTE: this module requires matplotlib

import matplotlib.pyplot as pyplot

# the size of the items to plot
size = 40

def create_plot(kmeans):
   # symbols, colors, and names
   symbols = ["s", "o", "^", ">", "v", "<", "d", "p", "h", "8", "+", "x"]
   colors = ["b", "y", "m", "r", "c", "g", "k", "w"]
   names = flatten([[o.name for o in cluster] for cluster in kmeans.clusters])

   # map of name -> symbol for plotting
   name_symbols = dict(zip(names, symbols))

   # create of dictionary of dictonaries of lists
   # [placed_cluster_number][item_name] -> list of objects
   plots = dict()
   for i, cluster in enumerate(kmeans.clusters):
      if i not in plots:
         plots[i] = dict()
      for o in cluster:
         if o.name not in plots[i]:
            plots[i][o.name] = []
         plots[i][o.name].append(o)

   # plot each configuration

   # make the plot
   figure = pyplot.figure()
   axis = figure.add_subplot(111)

   # for each cluster group found
   for cluster_number in plots:
      # for each name found within the cluster
      for name in plots[cluster_number]:
         values = plots[cluster_number][name]
         values = [list(o) for o in values]

         x_values = [o[0] for o in values]
         y_values = [o[1] for o in values]

         axis.scatter(x_values, y_values, s=size, c=colors[cluster_number], marker=name_symbols[name])

   # plot each centroid
   for centroid in kmeans.centroids:
      axis.scatter([centroid[0]], [centroid[1]], s=size, c='k', marker="+")

   pyplot.show()

def flatten(l):
   return set([item for sublist in l for item in sublist])
