#!/usr/bin/env python3
"""Defines a unittest module for utils.access_nested_map"""


import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map
from utils import get_json
from utils import memoize


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
        """Tests that the method returns what it is supposed to."""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        # Test case 4
        ({}, ("a",), "Key 'a' not found in the nested map"),

        # Test case 5
        ({"a": 1}, ("a", "b"), "Key 'b' not found in the nested map"),
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_exception_message):
        """Use the assertRaises context manager to test that a KeyError is
        raised"""
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
        """Tests that utils.get_json returns the expected result."""
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Implements the TestMemoize(unittest.TestCase) class with a
    test_memoize method"""
    class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        """Tests that when calling a_property twice, the correct result
        is returned but a_method is only called once
        using assert_called_once."""
        test_instance = self.TestClass()

        with patch.object(
                test_instance, 'a_method', return_value=42) as mock_a_method:
            r1 = test_instance.a_property()
            r2 = test_instance.a_property()

            mock_a_method.assert_called_once()
            self.assertEqual(r1, 42)
            self.assertEqual(r2, 42)


if __name__ == "__main__":
    unittest.main()
