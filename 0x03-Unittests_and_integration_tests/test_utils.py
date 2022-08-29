#!/usr/bin/env python3
"""
Unittest module to utils module
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map as anm
from utils import get_json, memoize
from typing import Mapping, Sequence, Any, Dict
from unittest.mock import MagicMock, patch


class TestAccessNestedMap(unittest.TestCase):
    """test class for acces_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence,
                               expected: Any) -> None:
        """function to test nested map"""
        self.assertEqual(anm(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """tests the exception Key Error"""
        with self.assertRaises(KeyError):
            anm(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get_json function"""

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict):
        """tests get json function"""

        with unittest.mock.patch('utils.requests.get') as mock_request:
            mock_response = MagicMock(status_code=200)
            mock_response.json.return_value = test_payload
            mock_request.return_value = mock_response
            func_response = get_json(test_url)
            mock_request.assert_called_once_with(test_url)
            self.assertEquals(func_response, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test that when calling a_property twice, the correct result is returned but
    a_method is only called once using assert_called_once.
    """

    def test_memoize(self):

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_val=42) as mock_object:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, mock_object.return_val)
            self.assertEqual(test_class.a_property, mock_object.return_val)
            mock_object.assert_called_once()

        unittest.__doc__