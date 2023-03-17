import numpy as np
import matplotlib.pyplot as plt

def analysis(num_devices, p):
    # Transition probability matrix
    P = np.zeros((num_devices+1, num_devices+1))
    for i in range(num_devices+1):
        for j in range(num_devices+1):
            if i == j:
                if i == 0:
                    P[i][j] = 1
                else:
                    P[i][j] = 1 - p
            elif j == i-1:
                P[i][j] = p
    
    # Calculate the inverse of the (I - Q) matrix
    I = np.identity(num_devices)
    Q = P[1:,1:]
    inv = np.linalg.inv(I - Q)
    
    # Calculate the expected number of slots to transmit all packets
    expected_slots = np.sum(inv[0])
    
    return expected_slots
