'''
network.py

A module to implement the stoxhastic gradient discent learning algorithm for a feedforward nerral network
Gradients are calculated using backpropagation.Note that I have focused on making the code simple,easily readable,and
easily modifiable.It is not optimized,and omits many desirable features.

'''

import random

import numpy as np

class Network(object):
    def __init__(self,sizes):
        """
        The list ''sizes''contains the number of neurons in the respective layers of the network.For
        example, if the list was [2,3,1] then it would be a three-layer network, with the first layer
        containing 2 neuron.the cecond layer 3 neurons,and the third layer 1 neuron.The biases and weights for
        the network are initialized randomly,using a Gaussian distribution with mean 0
        :param sizes:
        """