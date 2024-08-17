import unittest
import pandas as pd
import os

class TestImagePaths(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('Test_set_prediction_with_relative_image_paths_first_70_unique.csv')

    def test_image_paths_exist(self):
        for index, row in self.df.iterrows():
            image_path = row['image_path']
            
            self.assertIsNotNone(image_path, f"Image path is None for row {index}")
            
            self.assertTrue(os.path.exists(image_path), f"Image file does not exist: {image_path}")

    def test_unique_image_paths(self):
        image_paths = self.df['image_path'].tolist()
        unique_paths = set(image_paths)
        self.assertEqual(len(image_paths), len(unique_paths), "Duplicate image paths found")

    def test_correct_file_extension(self):
        for index, row in self.df.iterrows():
            image_path = row['image_path']
            self.assertTrue(image_path.lower().endswith('.jpg'), f"Incorrect file extension for row {index}: {image_path}")

if __name__ == '__main__':
    unittest.main()