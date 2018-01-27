'''
Created on Jan 27, 2018

@author: karan
'''


import gettingLongAndLat
import unittest

class testLat(unittest.TestCase):
    def test_checkLatitude(self):
        res= gettingLongAndLat.find()
        self.assertEqual(34.1656502, res,"Latituted doesn't match")
