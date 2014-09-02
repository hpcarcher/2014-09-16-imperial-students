#!/usr/bin/env python
#
# CFD Calculation
# ===============
#
# Simulation of flow in a 2D box using the Jacobi algorithm.
#
# Basic Python version - uses lists
#
# EPCC, 2014

import sys
import time
import ConfigParser

# Import the external jacobi function from "jacobi.py"
from jacobi import jacobi

def main(argv):

    # Test we have the correct number of arguments
    if len(argv) < 2:
        print "Usage: cfd.py <config file> <dat file> [quiet]"
        sys.exit(1)

    # Get command-line arguments.
    config_file = argv[0]
    dat_file = argv[1]
    quiet = (len(argv) == 3) and (argv[2] == "quiet")

    cfd(config_file, dat_file, quiet)

def cfd(config_file, dat_file, quiet=True):

    # Read and parse configuration file.
    config = ConfigParser.RawConfigParser()
    config.read(config_file)
    niter = config.getint('Simulation', 'iterations')
    edge = config.getint('Grid', 'edge')
    inlet_x = config.getint('Inlet', 'x')
    inlet_width = config.getint('Inlet', 'width')
    outlet_y = config.getint('Outlet', 'y')
    outlet_height = config.getint('Outlet', 'height')

    if (not quiet):
	sys.stdout.write("\n2D CFD Simulation\n")
	sys.stdout.write("=================\n")
	sys.stdout.write("   Iterations = {0}\n".format(niter))
	sys.stdout.write("         Edge = {0}\n".format(edge))
	sys.stdout.write("      Inlet X = {0}\n".format(inlet_x))
	sys.stdout.write("  Inlet width = {0}\n".format(inlet_width))
	sys.stdout.write("     Outlet Y = {0}\n".format(outlet_y))
	sys.stdout.write("Outlet height = {0}\n".format(outlet_height))

    # Time the initialisation
    tstart = time.time()

    # Set the dimensions of the array
    m = edge
    n = edge

    # Define the psi array and set it to zero
    psi = [[0 for col in range(m+2)] for row in range(n+2)]

    # Set the boundary conditions
    set_inlet_boundaries(psi, m, inlet_x, inlet_width)
    set_outlet_boundaries(psi, m, outlet_y, outlet_height)

    # Write the simulation details
    tend = time.time()
    if (not quiet):
	sys.stdout.write("\nInitialisation took {0:.5f}s\n".format(tend-tstart))
	sys.stdout.write("\nGrid size = {0} x {1}\n".format(m, n))
    
    # Call the Jacobi iterative loop (and calculate timings)
    if (not quiet):
	sys.stdout.write("\nStarting main Jacobi loop...\n")
    tstart = time.time()
    jacobi(niter, psi)
    tend = time.time()
    if (not quiet):
	sys.stdout.write("...finished\n")
	sys.stdout.write("\nCalculation took {0:.5f}s\n\n".format(tend-tstart))
    
    # Write the output file
    write_data(m, n, psi, dat_file)

    # Finish nicely
    sys.exit(0)

# Set the boundary conditions on top edge
def set_inlet_boundaries(psi, m, inlet_x, inlet_width):

    for i in range(inlet_x+1, inlet_x+inlet_width):
        psi[0][i] = float(i-inlet_x)
    for i in range(inlet_x+inlet_width, m+1):
        psi[0][i] = float(inlet_width)

# Set the boundary conditions on right edge
def set_outlet_boundaries(psi, m, outlet_y, outlet_height):

    for j in range(1, outlet_y+1):
        psi[j][m+1] = float(outlet_height)
    for j in range(outlet_y+1, outlet_y+outlet_height):
        psi[j][m+1] = float(outlet_height-j+outlet_y)

# Create a plot of the data using matplotlib
def write_data(m, n, psi, outfile):

    # Open the specified file
    out = open(outfile, "w")
    out.write("{0} {1}\n".format(m, n))
    # Loop over stream function matric (without boundaries)
    for i in range(1, m+1):
        for j in range(1, n+1):
            # Compute velocities and magnitude squared
            xvel = (psi[i][j+1] - psi[i][j-1])/2.0
            yvel = (psi[i-1][j] - psi[i+1][j])/2.0
            mvs = (xvel + yvel)**2
            # Scale the magnitude
            modvsq = mvs**0.3
            out.write("{0:5d} {1:5d} {2:10.5f} {3:10.5f} {4:10.5f}\n".format(i-1, j-1, xvel, yvel, modvsq))
    out.close()

# Function to create tidy way to have main method
if __name__ == "__main__":
        main(sys.argv[1:])

