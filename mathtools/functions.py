"""Useful mathematical functions
================================
This module provides functions postprocess data

"""

import numpy as np

def derivate(variable, function):
    """
    Make the derivation of function with respect to variable.
    Centered derivative except on both bounds where right derivative 
    and left derivative are performed. Thus the output has the same 
    length than function.
    variable : array
    function : array
    variable and function have to be of same size
    """

    derivFunc = np.zeros(len(function))
    derivFunc[0] = float(function[1]-function[0])/float(variable[1]-variable[0])
    derivFunc[-1] = float(function[-1]-function[-2])/float(variable[-1]-variable[-2])
    for i in range(1,len(function)-1):
        derivFunc[i] =  float(function[i+1]-function[i-1])/float(variable[i+1]-variable[i-1])

    return derivFunc

def integrate(variable, function, dz=None):
    """
    Integrate function as a function of variable.
    Integration by the method of trapeze
    """
    integral = 0.
    for k in range(len(function)-1):
        integral += (variable[k+1]-variable[k])*(function[k+1]+function[k])/2

    return integral

def integrate_slice(dz, function):
    """
    Integrate function over a grid which cells have width dz.
    """
    return sum(dz*function)

def primitive(variable, function):
    """
    Compute a primitive of function
    """
    primit = [0.0]
    for i in range(1,len(function)):
        primit.append(integrate(variable[:i], function[:i]))

    return np.array(primit)

def primitive_slice(dz, function):
    """
    Compute a primitive of function over a grid which cells
    width are dvariable
    """
    primit = np.zeros(len(function))
    for i in range(len(function)):
        primit[i] = (integrate_slice(dz[:i], function[:i])
                     + dz[i]/2 * function[i])
    return primit


def derivate_wall(variable, function, zwall=0, wall_value=0):
    """
    Make the derivation of function with respect to variable
    assuming a wall in zwall finite volume formulation.
    variable : 1D-array
    function : 1D-array
    zwall : float, wall position. Default assume a wall in 0.
    wall_value : float, value of variable at the wall. Default 0.
    top
    variable and function have to be of same size
    yf0  y0  yf1   y1   yf2    y2    yf3    ...
     ---------------------------------------------
     |   dz0  |    dz1   |     dz2    |     ...
     --------------------------------------------
    """

    #Build the grid at the face
    variable_f = np.zeros(len(variable)+1)
    dz = np.zeros(len(variable)+1)
    dz[0] = float(2*(variable[0]-zwall))
    for i in range(1, len(variable)):
        dz[i] = 2*(variable[i]-variable[i-1])-dz[i-1]
        variable_f[i] = variable_f[i-1] + dz[i-1]

    derivFunc_f = np.zeros(len(function)+1)
    for i in range(1, len(function)):
        derivFunc_f[i] = float(function[i]-function[i-1])/float(variable[i]-variable[i-1])
    derivFunc_f[0] = float(function[0]-wall_value)/float(variable[0]-zwall)
    
    #Interpolate on cell centers
    derivFunc = (derivFunc_f[:-1]+derivFunc_f[1:])/2
      
    return derivFunc
