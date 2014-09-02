# 
# Jacobi function for CFD calculation
#
# Basic Python version using lists
#
def jacobi(niter, psi):

    # Get the inner dimensions
    m = len(psi) - 2
    n = len(psi[0]) -2

    # Define the temporary array and zero it
    tmp = [[0 for col in range(m+2)] for row in range(n+2)]

    # Iterate for number of iterations
    for iter in range(niter):

        # Loop over the elements computing the stream function
        for i in range(1,m+1):
            for j in range(1,n+1):
                tmp[i][j] = 0.25 * (psi[i+1][j]+psi[i-1][j]+psi[i][j+1]+psi[i][j-1])

        # Update psi
        for i in range(1,m+1):
            for j in range(1,n+1):
                psi[i][j] = tmp[i][j]


