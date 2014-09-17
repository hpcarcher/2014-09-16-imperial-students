import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate

BIRTH = "birth"
DEATH = "death"
POPULATION = "population"

def update_population(population, time, prey, predator):
    '''
    Calculate the change in a population of predators and prey using
    the Lotka-Volterra equations at a single time-step.

    Parameters
    ----------

    population : array-like
        Current population of predators and prey as an array
        of form [current prey population, current predator
        population]. 
    time : float
        Time-step value.
    prey : dict
        Dictionary specifying prey behavior. This must hold floats
        indexed by keys BIRTH and DEATH, for prey birth and death
        rate.
    predator : dict
        Dictionary specifying predator behavior. This must hold floats
        indexed by keys BIRTH and DEATH, for predator birth and death
        rate.

    Returns
    -------

    output : array
        Array of form [new prey population, new predator population].
    '''
    return np.array([
        prey[BIRTH]*population[0] - 
            prey[DEATH]*population[0]*population[1],
        -predator[DEATH]*population[1] + 
            predator[BIRTH]*prey[DEATH]*population[0]*population[1]])

def simulate(prey, predator, end_time = 20, time_steps = 2000):
    '''
    Simulate the evolution of a population of predators and prey
    using the Lotka-Volterra equations.

    Parameters
    ----------

    prey : dict
        Dictionary specifying prey behavior. This must hold floats
        indexed by keys BIRTH and DEATH, for prey birth and death
        rate, and an integer indexed by key POPULATION for initial 
        population.
    predator : dict
        Dictionary specifying predator behavior. This must hold floats
        indexed by keys BIRTH and DEATH, for predator birth and death
        rate, and an integer indexed by key POPULATION for initial 
        population.
    end_time : scalar, optional
        End-time for simulation in seconds. Default 20.
    time_steps : int, optional
        Number of time-steps. Simulation values will be calculated
        from time==0 to time==end_time with time_steps - 2
        intermediate values. Default 2000.

    Returns
    -------
  
    output: array
        Array of time_steps elements where each element consists of
        the time at a specific time-step, the prey population at that
        time-step and the predator population at that time-step.
    '''
    time_series = np.linspace(0, end_time, time_steps)
    initial_population = np.array([prey[POPULATION], predator[POPULATION]])
    populations = integrate.odeint(
        update_population, 
        initial_population, 
        time_series, 
        args=(prey, predator))
    # Insert time_series as a new first column.
    return np.insert(populations, 0, time_series, axis=1)

def plot(data):
    '''
    Plot the change in predator and prey populations over time at
    intervals specified by a given time-series.

    Parameters
    ----------

    data: array
        Array of elements where each element consists of the time at a
        specific time-step, the prey population at that time-step and
        the predator population at that time-step. 
    '''
    fig = plt.figure()
    plt.plot(data[:,0], data[:,1], "r-", label="Prey")
    plt.plot(data[:,0], data[:,2], "b-", label="Predators")
    plt.grid()
    plt.legend(loc="best")
    plt.xlabel("time")
    plt.ylabel("population")
    plt.title("Evolution of predator and prey populations")
    plt.show()
