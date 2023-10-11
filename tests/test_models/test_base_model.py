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
