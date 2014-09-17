import sys

import numpy as np

from lotkavolterra import plot

def usage():
    '''Print usage information.'''
    print "Usage: python plot_lv.py DATA_FILE"
    print "View the results of a simulation of the evolution of a population of predators and prey using the Lotka-Volterra equations."
    print "This program inputs a CSV file with the time, prey population and predator population at each time-step"

if len(sys.argv) < 2:
    usage()
    sys.exit()
else:
    data_file = sys.argv[1]

data = np.loadtxt(data_file, delimiter=",")
plot(data)
