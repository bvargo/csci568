#!/usr/bin/env python

import csv

def read(filename="winners_losers.csv"):
   rows = []
   file = open(filename, 'rb')
   reader = csv.reader(file)
   for row in reader:
      if len(row):
         rows.append(row)
   return rows

def write(rows, filename="extended.csv"):
   flat_rows = [[' '.join(row[0]).replace("'", "")] + row[1:] for row in rows]
   with open(filename, 'wb') as f:
      writer = csv.writer(f)
      writer.writerows(flat_rows)

def num_parts_odd_even(row):
   if len(row[0]) % 2 == 0:
      row.append(True)
   else:
      row.append(False)
   return row

def contains_string(row, char):
   if char in ' '.join(row[0]):
      row.append(True)
   else:
      row.append(False)
   return row

def ratio_of_first_to_last(row):
   row.append(float(len(row[0][0])) / len(row[0][-1]))
   return row

def ratio_of_vowles(row):
   a = count_vowles(row[0][0])
   b = count_vowles(row[0][-1])
   if b == 0:
      row.append(0)
   else:
      row.append(float(a) / b)
   return row

def ratio_of_consonants(row):
   a = count_consonants(row[0][0])
   b = count_consonants(row[0][-1])
   if b == 0:
      row.append(0)
   else:
      row.append(float(a) / b)
   return row

def count_vowles(string):
    vowles = "aeiou"
    c = 0
    for letter in string:
       if letter in vowles:
          c += 1
    return c

def count_consonants(string):
    vowles = "aeiou"
    c = 0
    for letter in string:
       if letter not in vowles:
          c += 1
    return c

def starts_with_vowel(row):
   if row[0][0][0] in "aeiou":
      row.append(True)
   else:
      row.append(False)
   return row

def ends_with_vowel(row):
   if row[0][-1][-1] in "aeiou":
      row.append(True)
   else:
      row.append(False)
   return row

def num_uniq_letters(row):
   row.append(len(set(' '.join(row[0]))))
   return row

def number_of_vowel_digraphs(row):
   string = ' '.join(row[0])
   for i, letter in enumerate(string):
      if letter in 'aeiou':
         if i != len(string) - 1 and string[i+1] in 'aeiou':
            row.append(True)
            return row
   row.append(False)
   return row

def number_of_consant_digraphs(row):
   string = ' '.join(row[0])
   for i, letter in enumerate(string):
      if letter not in 'aeiou':
         if i != len(string) - 1 and string[i+1] not in 'aeiou':
            row.append(True)
            return row
   row.append(False)
   return row

def weighted_vowel_count(row):
   string = ' '.join(row[0])
   value = 0
   for i, letter in enumerate(string):
      if letter in 'aeiou':
         value += i
   row.append(value)
   return row

def consonant_digraph_beginning(row):
   string = ' '.join(row[0])
   if string[0] not in 'aeiou' and string[1] not in 'aeiou':
      row.append(True)
   else:
      row.append(False)
   return row

def consonant_digraph_end(row):
   string = row[0][-1]
   if string[0] not in 'aeiou' and string[1] not in 'aeiou':
      row.append(True)
   else:
      row.append(False)
   return row

def main():
   rows = read()
   rows = [[row[0].split(' '), True if row[1] == " + " else False] for row in rows]
   header = [["name"], "winner"]

   rows = map(lambda r: contains_string(r, '.'), rows)
   header.append("contains_dot")

   rows = map(lambda r: contains_string(r, '-'), rows)
   header.append("contains_dash")

   for function in [num_parts_odd_even, ratio_of_first_to_last, ratio_of_vowles, ratio_of_consonants, starts_with_vowel, ends_with_vowel, num_uniq_letters, number_of_vowel_digraphs, number_of_consant_digraphs, weighted_vowel_count, consonant_digraph_beginning, consonant_digraph_end]:
      rows = map(function, rows)
      header.append(function.__name__)

#   for row in rows:
#      print row

   write([header] + rows)

if __name__ == '__main__':
   main()
