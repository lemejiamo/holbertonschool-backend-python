#!/usr/bin/env python3
"""
Unittest module to utils module
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map as anm
from utils import get_json
from typing import Mapping, Sequence, Any, Dict
from unittest.mock import MagicMock


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
