#!/bin/bash

# Common words problem: read a text file, identify the N most
# frequently-occurring words, print out a sorted list of the words with
# their frequences. 

# Usage: wordcount.sh < FILE [N]

#  Bentley, Knuth, McIlroy 1986) Programming pearls: a literate
# program Communications of the ACM, 29(6), pp471-483, June
# 1986. http://dx.doi.org/10.1145/5948.315654. 
# Dr. Drang, More shell, less egg, December 4th, 2011.,
# http://www.leancrew.com/all-this/2011/12/more-shell-less-egg/ 

tr -cs A-Za-z '\n' | tr A-Z a-z | sort | uniq -c | sort -rn | sed ${1}q
