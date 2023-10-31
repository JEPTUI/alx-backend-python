#!/usr/bin/env python3
"""Defines a unittest module for utils.access_nested_map"""


import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map
from utils import get_json


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


class TestGetJson(unittest.TestCase):
    """Defines a class that implements TestGetJson.test_get_json method
    to test that utils.get_json returns the expected result"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            
            result = get_json(test_url)
            
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
