#!/usr/bin/python3
"""Test script for do_pack function"""

import unittest
from unittest.mock import patch
from datetime import datetime
from fabric.api import local
from os import path
import os


class TestDoPack(unittest.TestCase):
    """Test case for do_pack function"""

    @patch('datetime.datetime')
    def test_do_pack(self, mock_datetime):
        """Test do_pack function"""
        mock_datetime.now.return_value = datetime(2024, 4, 17, 12, 0, 0)
        

        from my_script import do_pack
        result = do_pack()

        self.assertTrue(result)
        
        self.assertTrue(path.exists(result))

        os.remove(result)

if __name__ == "__main__":
    unittest.main()
