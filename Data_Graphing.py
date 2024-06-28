#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import resample

# Load the data
file_path = r"file.csv" #Insert file path here
data = pd.read_csv(file_path, delimiter='\t', skiprows=2)

# Convert relevant columns to numeric, forcing errors to NaN
data = data.apply(pd.to_numeric, errors='coerce')

# Extract the relevant column for downsampling
column = data['m/(s^2)']

# Define original and target sampling rates
original_rate = 128  # Hz
target_rate = 60  # Hz

# Calculate the downsampling factor
downsample_factor = target_rate / original_rate

# Downsample the data using resampling
downsampled_data = resample(column, int(len(column) * downsample_factor))

#Adjusts display window
start_index = 31000
end_index = 34000

#Corrects if the end index is too high
if end_index > len(downsampled_data) - 1:
    end_index = len(downsampled_data) - 1


# Adjust the range for plotting
plot_data = downsampled_data[start_index:end_index]
plot_range = range(start_index, end_index)

#Plots data
plt.figure(figsize=(10, 5))
plt.plot(plot_range, plot_data)
plt.title('Example data')
plt.xlabel('Sample Index')
plt.ylabel('Acceleration (m/s^2)')
plt.grid(True)
plt.show()

