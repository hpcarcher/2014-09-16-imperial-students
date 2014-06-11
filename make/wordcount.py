#!/usr/bin/env python
 
import string
import sys

DELIMITERS = [".", ",", ";", ":", "?", "$", "@", "^", "<", ">", "#", "%", "`", "!", "*", "-", "=", "(", ")", "[", "]", "{", "}", "/", "\"", "\'"]

"""
Read lines from a plain-text file and return these concatenated
together in a single string.
"""
def get_text_from_file(file):
  text = ""
  f = open(file, "r")
  for line in f:
    text += line
  f.close()
  return text

"""
Given a string, return a dictionary of words and their frequency of
occurrence. TRANSLATE_TABLE is used first to replace DELIMITERS with
spaces before the string is broken into words. The function is
case-insensitive.
"""
def get_frequencies(text, min_length = 6):
  for purge in DELIMITERS:
    text = text.replace(purge, " ")
  words = text.split()
  frequencies = {}
  for word in words:
    word = word.lower().strip()
    if len(word) < min_length:
      continue
    if word in frequencies:
      frequencies[word] += 1
    else:
      frequencies[word] = 1
  return frequencies

"""
Print the contents of the given dictionary, one key value per line.
"""
def print_dictionary(dict):
  for key in dict:
    print key, dict[key]

"""
Print the contents of a list of pairs (a,b) one pair per line in the
form "a b"
"""
def print_pairs(pairs):
  for (a,b) in pairs:
    print a, b

"""
Read in a file, calculate the frequencies of each word in the file and
print the words and frequences in descending order.
"""
def word_count(file):
  text = get_text_from_file(file)
  frequencies = get_frequencies(text) 
  sorted_frequencies = sorted(frequencies.iteritems(), key=lambda (key,value): value, reverse=True)
  print_pairs(sorted_frequencies)

file=sys.argv[1]
word_count(file)
