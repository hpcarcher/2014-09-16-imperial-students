import getopt
import sys

from lotkavolterra import plot
from lotkavolterra import simulate
from lotkavolterra import BIRTH
from lotkavolterra import DEATH
from lotkavolterra import POPULATION

def usage():
    '''Print usage information.'''
    print "Usage: python simulate_and_plot_lv.py [options]"
    print "Options:"
    print "  -a N, --prey-birth=N      Natural growth rate of prey when there are no predators. Default: ", prey_birth
    print "  -b N, --prey-death=N      Natural death rate of prey due to predation. Default: ", prey_death
    print "  -c N, --predator-death=N  Natural death rate of predators when there are no prey. Default: ", predator_death
    print "  -d N, --predator-birth=N  How many prey have to be caught and eaten to produce a new predator. Default: ", predator_birth
    print "  -f N, --num-predators=N   Initial predator population. Default: ", num_predators
    print "  -r N, --num-prey=N        Initial prey population. Default: ", num_prey
    print "  -t N, --time=N            End time for simulation. Default: ", time
    print "  -n N, --time-steps=N      Number of time steps to run simulation for. Default: ", time_steps
    print "  -h, --help                Print this message and exit."
    print "Run a simulation of the evolution of a population of predators and prey using the Lotka-Volterra equations and plot the results."

flags = "a:b:c:d:f:r:t:n:h"
long_flags = ["prey-birth=", "prey-death=", "predator-death=",
    "predator-birth=", "num-predators=", "num-prey=",
    "time=", "time-steps=", "help"]

prey_birth = 1.0
prey_death = 0.1
predator_death = 1.5
predator_birth = 0.75
num_predators = 4
num_prey = 20
time = 20
time_steps = 2000

try:
    options, arguments = getopt.getopt(sys.argv[1:], flags, long_flags)
except getopt.GetoptError as err:
    usage()
    sys.exit()
for option, argument in options:
    if option in ("-h", "--help"):
        usage()
        sys.exit()
    elif option in ("-a", "--prey-birth"):
        prey_birth = float(argument)
    elif option in ("-b", "--prey-death"):
        prey_death = float(argument)
    elif option in ("-c", "--predator-death"):
        predator_death = float(argument)
    elif option in ("-d", "--predator-birth"):
        predator_birth = float(argument)
    elif option in ("-f", "--num-predators"):
        num_predators = float(argument)
    elif option in ("-r", "--num-prey"):
        num_prey = float(argument)
    elif option in ("-t", "--time"):
        time = float(argument)
    elif option in ("-n", "--time-steps"):
        time_steps = float(argument)

predator_config = {}
predator_config[BIRTH] = predator_birth
predator_config[DEATH] = predator_death
predator_config[POPULATION] = num_predators
prey_config = {}
prey_config[BIRTH] = prey_birth
prey_config[DEATH] = prey_death
prey_config[POPULATION] = num_prey

results = simulate(prey_config, predator_config, time, time_steps)
plot(results)
