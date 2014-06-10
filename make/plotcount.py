#!/usr/bin/env python
 
import numpy as np
import matplotlib.pyplot as plt
import string
import sys

"""
Read lines from a plain-text file with lines of form "WORD FREQUENCY"
and return these as an ordered list of frequencies.
"""
def get_frequencies_from_file(file):
  frequencies = []
  f = open(file, "r")
  for line in f:
    fields = line.split()
    frequencies.append((fields[0], int(fields[1])))
  f.close()
  return frequencies

"""
Given a list of frequencies (WORD, FREQUENCY), plot these as a histogram.
Only the first limit frequencies are plotted.
"""
def plot_frequencies(frequencies, limit = 10):
  plt.title("Frequencies")
  limited_frequencies = frequencies[0:limit]
  words = [word for (word, count) in limited_frequencies]
  counts = [count for (word, count) in limited_frequencies]
  position = np.arange(len(words))
  width = 1.0
  ax = plt.axes()
  ax.set_xticks(position + (width/2))
  ax.set_xticklabels(words)
  plt.bar(position, counts, width, color='b')

"""
Given a list of frequencies (WORD, FREQUENCY), plot these as a histogram then
show the histogram.
Only the first limit frequencies are plotted.
"""
def plot_and_show_frequencies(file):
  frequencies = get_frequencies_from_file(file)
  plot_frequencies(frequencies)
  plt.show()

"""
Given a list of frequencies (WORD, FREQUENCY), plot these as a histogram then
save the histogram as an image file. Only the first limit frequencies are
plotted. savefile's extension determines the image type.
"""
def plot_and_save_frequencies(file, savefile):
  frequencies = get_frequencies_from_file(file)
  plot_frequencies(frequencies)
  plt.savefig(savefile)

def show_usage():
  print "Usage: plotcount.py [-show|-save] FILE [SAVEFILE]"
  exit()

if len(sys.argv) < 3:
  show_usage()
  exit()
command = sys.argv[1]
if (command == "-show"):
  plot_and_show_frequencies(sys.argv[2])
elif (command == "-save") and (len(sys.argv) >= 4):
  plot_and_save_frequencies(sys.argv[2], sys.argv[3])
else:
  show_usage()
  exit()
