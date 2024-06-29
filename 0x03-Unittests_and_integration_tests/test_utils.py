#!/usr/bin/env python3
"""First Task"""
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from unittest import main, TestCase, mock
from parameterized import parameterized


class TestAccessNestedMap(TestCase):
    """Test cases for the access_nested_map function.

    This class contains tests to ensure the access_nested_map function
    works correctly for various inputs.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any) -> None:
        """Test access_nested_map with different nested maps and paths.

        Args:
            nested_map (Mapping): A nested dictionary from which to access
            a value.
            path (Sequence): A sequence of keys representing the path to
            the value.
            expected (Any): The expected value at the end of the path.

        Asserts:
            That access_nested_map(nested_map, path) returns the expected value
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """_summary_

        Args:
            nested_map (Mapping): _description_
            path (Sequence): _description_
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """_summary_

    Args:
        TestCase (_type_): _description_
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @mock.patch("utils.requests.get")
    def test_get_json(self, test_url: str, test_payload: object, url_get: Any):
        """_summary_

        Args:
            test_url (_type_): _description_
            test_payload (_type_): _description_
        """
        response = mock.Mock()
        response.json.return_value = test_payload
        url_get.return_value = response

        result = get_json(test_url)

        # url_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(TestCase):
    def test_memoize(self):
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()


if __name__ == "__main__":
    """Entry Point"""
    main()
