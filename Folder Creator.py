#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

def create_and_rename_folders(base_path, folder_structure, rename_map):
    for folder_path in folder_structure:
        # Split the folder path into parts
        folder_parts = folder_path.split("\\")
        # Rename parts based on the rename map
        renamed_parts = [rename_map.get(part, part) for part in folder_parts]
        # Join the renamed parts to form the new folder path
        renamed_path = os.path.join(base_path, *renamed_parts)
        try:
            os.makedirs(renamed_path, exist_ok=True)
            print(f"Folder created successfully at: {renamed_path}")
        except Exception as e:
            print(f"An error occurred while creating {renamed_path}: {e}")

# Example usage
#Load the data

file_path = [r"C:\Users\grays\Desktop\570_HEAL_156_Session1_LeftAnk_0000_Calibrated_PC.csv",
r"C:\Users\grays\Desktop\570_HEAL_156_Session1_LeftAnkle_Calibrated_PC.csv",
r"C:\Users\grays\Desktop\570_HEAL_156_Session1_RightAnkle_Calibrated_PC.csv",
r"C:\Users\grays\Desktop\570_HEAL_156_Session1_RightWrist_Calibrated_PC.csv",
r"C:\Users\grays\Desktop\570_HEAL_156_Session1_LeftWrist_Calibrated_PC.csv"]

#Define Changes
walk_jog_change = 20500
jog_run_change = 32250


#Define patient id
patient_id = "570_HEAL_156"

#Defines base path
base_path = r"C:\Users\grays\Desktop"

# Define the size of each subset
subset_size = 600

folder_structure = [
    "folder0",
    "folder1\subfolder1",
    "folder1\subfolder2",
    "folder1\subfolder3",
    "folder2\subfolder4",
    "folder2\subfolder5",
    "folder2\subfolder6",
    "folder3\subfolder7",
    "folder3\subfolder8",
    "folder3\subfolder9",
    "folder4\subfolder10",
    "folder4\subfolder11",
    "folder4\subfolder12",
    "folder5\subfolder13",
    "folder5\subfolder14",
    "folder5\subfolder15",
]

# Dictionary to rename folders
rename_map = {
    "folder0": f"{patient_id}_Slices",
    "folder1": f"{patient_id}_Sacrum",
    "folder2": f"{patient_id}_Left_Wrist",
    "folder3": f"{patient_id}_Left_Ankle",
    "folder4": f"{patient_id}_Right_Wrist",
    "folder5": f"{patient_id}_Right_Ankle",
    "subfolder1": f"{patient_id}_Sacrum_Walking",
    "subfolder2": f"{patient_id}_Sacrum_Jogging",
    "subfolder3": f"{patient_id}_Sacrum_Running",
    "subfolder4": f"{patient_id}_Left_Wrist_Walking",
    "subfolder5": f"{patient_id}_Left_Wrist_Jogging",
    "subfolder6": f"{patient_id}_Left_Wrist_Running",
    "subfolder7": f"{patient_id}_Left_Ankle_Walking",
    "subfolder8": f"{patient_id}_Left_Ankle_Jogging",
    "subfolder9": f"{patient_id}_Left_Ankle_Running",
    "subfolder10": f"{patient_id}_Right_Wrist_Walking",
    "subfolder11": f"{patient_id}_Right_Wrist_Jogging",
    "subfolder12": f"{patient_id}_Right_Wrist_Running",
    "subfolder13": f"{patient_id}_Right_Ankle_Walking",
    "subfolder14": f"{patient_id}_Right_Ankle_Jogging",
    "subfolder15": f"{patient_id}_Right_Ankle_Running",
}

create_and_rename_folders(base_path, folder_structure, rename_map)

