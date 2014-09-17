import ConfigParser
import os
import sys
import time

import numpy as np

from lotkavolterra import plot
from lotkavolterra import simulate
from lotkavolterra import BIRTH
from lotkavolterra import DEATH
from lotkavolterra import POPULATION

PREDATOR = "Predator"
PREY = "Prey"
SIMULATION = "Simulation"
TIME = "time"
TIME_STEPS = "time_steps"

def usage():
    print "Usage: python simulate_lv.py CONFIG_FILE OUTPUT_FILE"
    print "Run a simulation of the evolution of a population of predators and prey using the Lotka-Volterra equations."
    print "This program inputs a configuration file with the configuration parameters and outputs a CSV file with the time, prey population and predator population at each time-step"
    print "The configuration file should be of form:"
    print "[Prey]"
    print "birth = 1.0"
    print "death = 0.1"
    print "population = 20"
    print "[Predator]"
    print "death = 1.5"
    print "birth = 0.75"
    print "population = 4"
    print "[Simulation]"
    print "time = 20"
    print "time_steps = 2000"

def get_animal_config(config, animal_type):
    animal = {}
    animal[BIRTH] = config.getfloat(animal_type, BIRTH)
    animal[DEATH] = config.getfloat(animal_type, DEATH)
    animal[POPULATION] = config.getint(animal_type, POPULATION)
    return animal

if len(sys.argv) < 3:
    usage()
    sys.exit()
else:
    config_file = sys.argv[1]
    output_file = sys.argv[2]

config = ConfigParser.RawConfigParser()
config.read(config_file)
prey_config = get_animal_config(config, PREY)
predator_config = get_animal_config(config, PREDATOR)
end_time = config.getfloat(SIMULATION, TIME)
time_steps = config.getint(SIMULATION, TIME_STEPS)

results = simulate(prey_config, predator_config, end_time, time_steps)

header = "Predator-prey Lotka-Volterra simulation data\n"
header += "Produced by " + os.path.basename(__file__) + " on " + \
    time.asctime( time.localtime(time.time()))
header += "\nTime-step, predator population, prey population"
np.savetxt(output_file, results, delimiter=",", header=header)
