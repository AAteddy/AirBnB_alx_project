#!/usr/bin/bash
"""Defines a unittest test module for BaseModel class
in models/base_model.py.

Unittest classes: 
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""

import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittest for testing BaseModel class instantiation."""

    def test_no_args_instantiation(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    """def test_new_instance_stored_in_objets(self): 
        self.assertIn(BaseModel(), models.storage.all().values())"""

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)


if __name__ == "__main__":
    unittest.main()
