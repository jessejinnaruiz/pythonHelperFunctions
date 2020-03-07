import random

# Goal is to create 13 groups of 5 randomly generated integers 

# create enply list
list_of_samples = []

# for loop that creates a random group of 5 integers between (0-12) 12 times
# so each group looks like [0,2,11,9,3] or similar
for i in range(12):
    sample = random.sample(range(0,12), 5)
    # add the groups to the list_of_samples
    list_of_samples.append(sample)

# Create new file
file = open('sample.txt', 'w')

# Write the parts of the list_of_samples to the file
for element in list_of_samples:
    file.write(str(element))
