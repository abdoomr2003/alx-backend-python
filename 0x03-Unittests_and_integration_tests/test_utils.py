#!/usr/bin/env python3
"""First Task"""
from utils import access_nested_map
from typing import Mapping, Sequence, Any
from unittest import main, TestCase
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


if __name__ == "__main__":
    """Entry Point"""
    main()
