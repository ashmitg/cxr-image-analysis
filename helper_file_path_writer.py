import pandas as pd
import os

# Load the DataFrame
df = pd.read_csv('Test_set_prediction.csv')

base_dir = 'cxr-image-analysis/files'  

def generate_file_paths(subject_id, base_dir):
    subject_id_str = str(subject_id)
    p = subject_id_str[:2]
    subject_dir = os.path.join(base_dir, f'p{p}', f'p{subject_id_str}')
    
    if os.path.exists(subject_dir):
        image_files = []
        for root, dirs, files in os.walk(subject_dir):
            for file in files:
                if file.endswith('.jpg'):
                    # Create relative path
                    rel_path = os.path.relpath(os.path.join(root, file), start=os.getcwd())
                    image_files.append(rel_path)
        return sorted(image_files)
    return []

unique_subject_ids = df['subject_id'].unique()[:70]

all_image_paths = {subject_id: generate_file_paths(subject_id, base_dir) for subject_id in unique_subject_ids}

def assign_image_path(row, image_paths):
    subject_id = row['subject_id']
    if subject_id in image_paths and image_paths[subject_id]:
        path = image_paths[subject_id].pop(0)
        if not image_paths[subject_id]:
            del image_paths[subject_id]
        return path
    return None

# Assign image paths to the DataFrame
df['image_path'] = df.apply(lambda row: assign_image_path(row, all_image_paths), axis=1)

df = df.dropna(subset=['image_path'])

print(df[['subject_id', 'image_path']])

df.to_csv('Test_set_prediction_with_relative_image_paths_first_70_unique.csv', index=False)