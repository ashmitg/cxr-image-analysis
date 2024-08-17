#scraped the first 70 unique subject_ids from the Test_set_prediction.csv file and downloaded the images from the physionet website since it was not possible for me to download 500gb of data on my local machine.

import pandas as pd
import os
from tqdm import tqdm

df = pd.read_csv('Test_set_prediction.csv')

df = df.drop_duplicates(subset='subject_id')
print(df.head())
total_rows = df.shape[0]

for i, (_, row) in enumerate(tqdm(df.iterrows(), total=total_rows, desc='Downloading files')):
    subject_id = str(row['subject_id'])
    p = subject_id[:2]
    
    url = f'https://physionet.org/files/mimic-cxr-jpg/2.1.0/files/p{p}/p{subject_id}/'    
    cmd = f'wget -r -N -c -np {url} > /dev/null 2>&1'
    
    os.system(cmd)
    tqdm.write(f'Processed {i+1} of {total_rows} files')
