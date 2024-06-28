#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from scipy.signal import resample
import os

def create_and_rename_folders(base_path, folder_structure, rename_map):
    for folder_path in folder_structure:
        # Split the folder path into parts
        folder_parts = folder_path.split(os.sep)
        # Rename parts based on the rename map
        renamed_parts = [rename_map.get(part, part) for part in folder_parts]
        # Join the renamed parts to form the new folder path
        renamed_path = os.path.join(base_path, *renamed_parts)
        try:
            os.makedirs(renamed_path, exist_ok=True)
            print(f"Folder created successfully at: {renamed_path}")
        except Exception as e:
            print(f"An error occurred while creating {renamed_path}: {e}")

def downsamples_data(file_path):
    data = pd.read_csv(file_path, delimiter='\t', skiprows=2)

    # Convert all columns to numeric, forcing errors to NaN
    data = data.apply(pd.to_numeric, errors='coerce')

    # Define original and target sampling rates
    original_rate = 128  # Hz
    target_rate = 60  # Hz

    # Calculate the downsampling factor
    downsample_factor = target_rate / original_rate

    # Remove unnamed columns
    data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

    # Initialize a DataFrame to store downsampled data
    downsampled_data = pd.DataFrame()

    # Downsample each column except 'ms' which is the time column
    for column in data.columns:
        if column == 'ms':
            # Generate new time points for downsampled data
            downsampled_data['ms'] = np.linspace(data['ms'].iloc[0], data['ms'].iloc[-1], int(len(data) * downsample_factor))
        else:
            downsampled_data[column] = resample(data[column], int(len(data[column]) * downsample_factor))
    return downsampled_data

# Loop over each subset
def generates_CSV_files(total_subsets, start_index, end_index, downsampled_data, sensor, movement,patient_id, csv_file_path):
    for i in range(total_subsets):
        # Select range of rows for the current subset
        start_row = start_index + i * subset_size
        end_row = min(start_index + (i + 1) * subset_size, end_index + 1)  # Ensure not to exceed the end index

        # Select subset of downsampled data
        subset_downsampled_data = downsampled_data.iloc[start_row:end_row]

        # Define the file path for the CSV file
        csv_file = csv_file_path
        csv_file_path = csv_file_path + rf"_{start_index + i * subset_size}.csv"

        # Export the subset of downsampled data to a CSV file
        subset_downsampled_data.to_csv(csv_file_path, index=False)

        print(f"Subset {i+1}/{total_subsets} data has been exported to:", csv_file_path)
        csv_file_path = csv_file


for file in file_path:
    downsampled_data = downsamples_data(file)
    
    if jog_run_change > len(downsampled_data) - 1:
        jog_run_change = len(downsampled_data) - 1
        
    if walk_jog_change > len(downsampled_data) - 1:
        walk_jog_change = len(downsampled_data) - 1
    if "0000" in file:
        sensor = "Sacrum"
    elif "Ankle" in file:
        if "Right" in file:
            sensor = "Right_Ankle"
        else:
            sensor = "Right_Wrist"
    elif "Wrist" in file:
        if "Left" in file:
            sensor = "Left_Ankle"
        else:
            sensor = "Left_Wrist"
    elif "Shimmer" in file:
        sensor = "Right_Wrist"
    else:
        sensor = "Sacrum"
            
    for i in range(3):
        if i == 0:
            movement = "Walking"
            start_index = 0
            end_index = walk_jog_change
        elif i == 1:
            movement = "Jogging"
            start_index = walk_jog_change
            end_index = jog_run_change
        else:
            movement = "Running"
            start_index = jog_run_change
            end_index = len(downsampled_data) - 1
        
        # Calculate the total number of subsets based on the start and end indices
        total_subsets = (end_index - start_index + 1) // subset_size
        
        csv_file_path = rf"Start of path_{patient_id}_{sensor}\{patient_id}_{sensor}_{movement}\{patient_id}_{sensor}_{movement}"

        generates_CSV_files(total_subsets, start_index, end_index, downsampled_data, sensor, movement, patient_id, csv_file_path)

