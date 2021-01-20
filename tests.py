import unittest
import csv
from unittest.mock import patch
from script import proc_csv

class TestClass(unittest.TestCase):
    def test_csv_reader(self):
        self.data = 'Python Developer Test Dataset.csv'
        with open(self.data) as f:
            reader = csv.reader(f, delimiter=',')
            new_csv = list(reader).copy()
            self.assertEqual(new_csv[0], ['Property Name', 'Property Address [1]', 'Property  Address [2]', 'Property Address [3]', 'Property Address [4]', 'Unit Name', 'Tenant Name', 'Lease Start Date', 'Lease End Date', 'Lease Years', 'Current Rent'])
            self.assertTrue(new_csv, list)
    
    def test_proc_csv(self):
        with patch('builtins.input', return_value=1) as fake_out:
            doc = proc_csv('Python Developer Test Dataset.csv')
            self.assertTrue(doc, list)
            
            
    
    
unittest.main()