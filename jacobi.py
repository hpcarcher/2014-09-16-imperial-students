"""
Computational Fluid Dynamics JACOBI functions.

Written by EPCC 2014.
"""

def jacobi(num_iterations, psi):
    """
    Update stream function across a number of iterations.

    Keyword arguments:
    num_iterations -- number of iterations.
    psi -- 2D array of initial stream function values.
    """
    
    # Get the box dimensions.
    height = len(psi) - 2
    width = len(psi[0]) - 2
    
    tmp = [[0 for col in range(width+2)] for row in range(height+2)]

    iteration = 0
    while iteration < num_iterations:
	update_stream_function(width, height, psi, tmp)
	iteration += 1

def update_stream_function(width, height, psi, tmp):
    """
    Update stream function over a single iteration.

    Keyword arguments:
    width -- box width.
    height -- box height.
    psi -- 2D array of stream function values.
    tmp -- 2D array of temporary stream function values.
    """

    # Calculate updated stream function into tmp.
    i = 1
    while i < height + 1:
	j = 1
	while j < width + 1:
	    tmp[i][j] = 0.25 * (psi[i+1][j]+psi[i-1][j]+psi[i][j+1]+psi[i][j-1])
	    j += 1
	i += 1

    # Update stream function using tmp.
    i = 1
    while i < height + 1:
	j = 1
	while j < width + 1:
	    psi[i][j] = tmp[i][j]
	    j += 1
	i += 1
