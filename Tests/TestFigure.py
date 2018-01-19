import unittest

from Search.Figure import *

class TestFigure(unittest.TestCase):
    def test_init(self):
        self.assertRaises(FigureError,Figure,[(42,42)])
        self.assertRaises(FigureError,Figure,[(42,42),(42,42)])
        self.assertEqual(Figure([(0,0),(42,0),(42,42)])._vertexes,[(0,0),(42,0),(42,42)])
