#!/usr/bin/python3
"""
Module for unittests for the Base class base.py
"""
import os
import unittest
from models.base import Base


class TestBaseClassCreation(unittest.TestCase):
    """Task 1 Cases: Test class for Base class instantiation tests"""

    def test_id_positive(self):
        bo = Base(23)
        self.assertEqual(bo.id, 23)
        bo = Base(34)
        self.assertEqual(bo.id, 34)

    def test_id_negative(self):
        bo = Base(-4)
        self.assertEqual(bo.id, -4)
        bo = Base(-10)
        self.assertEqual(bo.id, -10)

    def test_id_none(self):
        bo = Base()
        self.assertEqual(bo.id, 1)
        bo = Base(None)
        self.assertEqual(bo.id, 2)

    def test_id_string(self):
        bo = Base("st")
        self.assertEqual(bo.id, "st")
        bo = Base("st2")
        self.assertEqual(bo.id, "st2")

    def test_id_float(self):
        bo = Base(0.5)
        self.assertEqual(bo.id, 0.5)
        bo = Base(2.4)
        self.assertEqual(bo.id, 2.4)
        """End Task 1"""
