#!/usr/bin/env python3
"""Defines a unittest module for utils.access_nested_map"""


import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Defines a class that inherits from unittest.TestCase"""
    @parameterized.expand([
        # Test case 1
        ({"a": 1}, ("a",), 1),

        # Test case 2
        ({"a": {"b": 2}}, ("a",), {"b": 2}),

        # Test case 3
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        # Test case 4
        ({}, ("a",), "Key 'a' not found in the nested map"),

        # Test case 5
        ({"a": 1}, ("a", "b"), "Key 'b' not found in the nested map"),
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_exception_message):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_exception_message)


if __name__ == "__main__":
    unittest.main()
