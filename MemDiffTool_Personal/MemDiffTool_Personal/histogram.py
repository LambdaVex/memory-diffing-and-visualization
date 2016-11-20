import numpy as NP

column_of_values = NP.random.randint(0, 50, 50)
print(column_of_values)
print("\n")
# set the bin values:
bins = NP.array(range(0,50))
print(bins)
print("\n")
binned_values = NP.digitize(column_of_values, bins)
print(binned_values)
print("\n")
print(NP.bincount(binned_values))



