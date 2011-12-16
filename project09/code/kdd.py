#!/usr/bin/env python

from operator import itemgetter

from load_data import load

# returns a 2-tuple of the similarity between two users
#   first element is the scoring difference, where 0 is identical and a positive
#     score is a sum-squared difference; if nothing in common, None
#   second element is the number of items in common that contribued to error
def user_similarity(user1, user2, ratings):
   user1 = ratings[user1]
   user2 = ratings[user2]

   sse = 0

   common_items = set(user1.keys()) & set(user2.keys())
   for item in common_items:
      sse += pow(user1[item] - user2[item], 2)
   if len(common_items) == 0:
      sse = None

   return sse, len(common_items)

# generates a dictionary of user -> list of 3-tuples, where the 3-tuple
# contains (similar_user_id, similarity, support); the list is sorted such
# that the most similar user is first
# if min_support is provided, only users whose support is greater than 0 are
# included
# if max_similarity is provided, then only users whose similarity is better
# than max_similarity are included
def generate_similar_users(ratings, min_support=0, max_similarity=None):
   similarities = dict()

   # generate ratings
   for user1 in ratings:
      for user2 in ratings:
         if user1 < user2:
            if user1 not in similarities:
               similarities[user1] = []
            if user2 not in similarities:
               similarities[user2] = []

            similarity, support = user_similarity(user1, user2, ratings)
            if support > min_support:
               if not max_similarity or similarity < max_similarity:
                  similarities[user1].append((user2, similarity, support))
                  similarities[user2].append((user1, similarity, support))

   # sort for each user based on similarity (best first) and then support
   # (best first)
   for user in similarities:
      # stable sort, so sort the second-level sort first
      similarities[user].sort(key=itemgetter(2), reverse=True)
      similarities[user].sort(key=itemgetter(1))

   return similarities

# predict the rating that user would rate an item, based off of user
# similarities
# if num_required is provided, then the number of similar users used will be
# <= num_similarities
# returns a 2-tuple of (rating, support)
def predict_rating(user, item, ratings, similarities, num_similarities=5):
   # ratings from like-users, limited by num_similarities
   # rating, similarity, support
   mratings = []

   for ouser, similarity, support in similarities[user]:
      if len(mratings) == num_similarities:
         break

      if item in ratings[ouser]:
         mratings.append((ratings[ouser][item], similarity, support))

   if not mratings:
      # if no similar users, cannot compute a rating; return an average rating
      # of 50
      return 50, 0
   elif len(mratings) == 1:
      # if only one user, return that rating
      return mratings[0][0], 1

   # more than one user - weight based on similarity and support

   # compute most similar and least similar score
   most_similar = min([a[1] for a in mratings])
   least_similar = max([a[1] for a in mratings])

   # weight each rating
   rating = 0
   total = 0
   for rate, similarity, support in mratings:
      rating += rate * (least_similar - similarity + 1) * support
      total += 100 * (least_similar - similarity + 1) * support

   rating = float(rating) / total * 100
   # round to the nearest 10
   rating = round(rating, -1)
   return rating, len(mratings)

def main():
   # load data
   print "Loading..."
   objects, training, validation = load()

   # calculate similarities
   print "Calculating similarities..."
   similarities = generate_similar_users(training, min_support=5)

   # see how well predict_rating performs
   print "Validating..."
   error = 0
   error2 = 0 # error from only cases where we could give a rating
   num_validations = 0
   for user in validation:
      for item in validation[user]:
         p = predict_rating(user, item, training, similarities)
         a = validation[user][item]
         error += abs(p[0] - a)
         num_validations += 1
         if p[1]:
            error2 += abs(p[0] - a)
         #print "Predicted: %0.2f,\t Actual: %0.2f" % (p[0], a)
   print "Error, on average, was %0.2f" % (error/num_validations)
   print "Error, excluding not enough data cases, was, on average, %0.2f" % (error2/num_validations)

if __name__ == "__main__":
   main()
