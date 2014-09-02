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
    iter = 0
    while iter < niter:

        # Loop over the elements computing the stream function
        i = 1
        while i < m + 1:
            j = 1
            while j < n + 1:
                tmp[i][j] = 0.25 * (psi[i+1][j]+psi[i-1][j]+psi[i][j+1]+psi[i][j-1])
                j +=1
            i +=1

        # Update psi
        i = 1
        while i < m + 1:
            j = 1
            while j < n + 1:
                psi[i][j] = tmp[i][j]
                j += 1
            i += 1

        iter += 1
