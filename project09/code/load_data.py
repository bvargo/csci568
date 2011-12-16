#!/usr/bin/env python

# loads data from the following filfes
# ../data/albumData1.txt
# ../data/artistData1.txt
# ../data/genreData1.txt
# ../data/trackData1.txt
#
# trainIdx1.firstLines.txt, for training
# validationIdx1.firstLines.txt, for validation
# testIdx1.firstLines.txt, for testing

from models import *

# returns 3-tuple of objects, training, and validation
def load():
   # all objects and a list of associated objects (one-way)
   # a map of id -> associated ids (artists, genres, etc)
   objects = dict()

   # training ratings
   # a map of user id -> (map of item -> rating)
   training = dict()

   # validation ratings
   # a map of user id -> list of 2-tuples containing (item, rating)
   validation = dict()

   load_albums(objects)
   load_tracks(objects)

   load_full_ratings(training, "../data/trainIdx1.firstLines.txt")
   load_full_ratings(validation, "../data/validationIdx1.firstLines.txt")
   #load_full_ratings(training, "../data/trainIdx1.txt")
   #load_full_ratings(validation, "../data/validationIdx1.txt")

   return objects, training, validation

def load_albums(objects):
   # read the data file
   f = open("../data/albumData1.txt", "r")

   # process each line without loading the entire file into memory at once
   for line in f:
      # remove the ending newline
      line = line[:-1]

      # get id, artist, genres
      parts = line.split("|")
      id = parts[0]
      artist = parts[1]
      genres = parts[2:]

      # add the album id with genres
      objects[id] = map(int, genres)

      # add the artist, if it exists
      if artist != "None":
         objects[id].insert(0, int(artist))

   f.close()

def load_tracks(objects):
   # read the data file
   f = open("../data/trackData1.txt", "r")

   # process each line
   for line in f:
      # remove the ending newline
      line = line[:-1]

      # get id, album, artist, genres
      parts = line.split("|")
      id = parts[0]
      album = parts[1]
      artist = parts[2]
      genres = parts[3:]

      # add the track id with associated genres
      objects[id] = map(int, genres)

      # add associated artist, if it exists
      if artist != "None":
         objects[id].insert(0, int(artist))

      # add associated album, if it exists
      if album != "None":
         objects[id].insert(0, int(album))

   f.close()

def load_full_ratings(ratings, filename):
   # read the data file
   f = open(filename, "r")

   # current user being processed
   user = None

   # process each line
   for line in f:
      # remove newline
      line = line[:-1]

      if "|" in line:
         # new user
         parts = line.split("|")
         user = int(parts[0])
         ratings[user] = dict()
      else:
         # add to existing user
         parts = line.split("\t")
         item = int(parts[0])
         rating = int(parts[1])
         ratings[user][item] = rating

   f.close()

if __name__ == "__main__":
   load()
