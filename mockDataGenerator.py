import numpy as np

# using numpy's random module to grab randomly generated floats between 0-2.3
sample = np.random.uniform(low=0, high=2.3, size=1000)

# now save this large set to a csv file using numpy savetxt
with open('mockData.txt', 'w') as my_data_file:
    np.savetxt(my_data_file, sample)
