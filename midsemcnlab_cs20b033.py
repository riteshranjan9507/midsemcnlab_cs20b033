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
def simulation(num_devices, p):
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
    
    # Generate 1000 random initial states
    initial_states = np.random.randint(1, num_devices+1, size=1000)
    
    # Simulate the Markov chain for each initial state
    num_slots = []
    for init_state in initial_states:
        curr_state = init_state
        num_steps = 0
        while curr_state != 0:
            curr_state = np.random.choice(range(num_devices+1), p=P[curr_state])
            num_steps += 1
        num_slots.append(num_steps)
       # Calculate the average number of slots over the 1000 runs
    avg_slots = np.mean(num_slots)
    
    return avg_slots
