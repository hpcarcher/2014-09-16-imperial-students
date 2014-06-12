#!/usr/bin/env python
 
import string
import sys

DEFAULT_MIN_LENGTH = 6
DELIMITERS = [".", ",", ";", ":", "?", "$", "@", "^", "<", ">", "#", "%", "`", "!", "*", "-", "=", "(", ")", "[", "]", "{", "}", "/", "\"", "\'"]

"""
Read lines from a plain-text file and return these as a list, with
trailing newlines stripped.
"""
def load_text(file):
  text = ""
  with open(file) as f:
    lines = f.read().splitlines()
  return lines

"""
Given a string, update a dictionary of words and their frequency of
occurrence. DELIMITERS are removed before the string is broken into
words. The function is case-insensitive. Words with length less than
min_length are omitted.
"""
def add_frequencies(line, frequencies, min_length = DEFAULT_MIN_LENGTH):
  for purge in DELIMITERS:
    line = line.replace(purge, " ")
  words = line.split()
  for word in words:
    word = word.lower().strip()
    if len(word) < min_length:
      continue
    if word in frequencies:
      frequencies[word] += 1
    else:
      frequencies[word] = 1

"""
Given a list of strings, return a dictionary of words and their frequency of  
occurrence. The function is case-insensitive. Words with length less
than min_length are omitted.
"""
def get_frequencies(lines, min_length = DEFAULT_MIN_LENGTH):
  frequencies = {}
  for line in lines:
    add_frequencies(line, frequencies, min_length)
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
Print the contents of a list of pairs (a,b) one pair per line in the
form "a b" to a file.
"""
def save_pairs(file, pairs):
  f = open(file, 'w')
  for (a,b) in pairs:
    f.write("%s %d\n" % (a, b))
  f.close()

"""
Read in a file, calculate the frequencies of each word in the file and
save in a new file the words and frequences in descending order.
"""
def word_count(input_file, output_file, min_length):
  text = load_text(input_file)
  frequencies = get_frequencies(text, min_length) 
  sorted_frequencies = sorted(frequencies.iteritems(), key=lambda (key,value): value, reverse=True)
  save_pairs(output_file, sorted_frequencies)

input_file=sys.argv[1]
output_file=sys.argv[2]
limit = DEFAULT_MIN_LENGTH
if (len(sys.argv) > 3):
  limit = int(sys.argv[3])
word_count(input_file, output_file, limit)
