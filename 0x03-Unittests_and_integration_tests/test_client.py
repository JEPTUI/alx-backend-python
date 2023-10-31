#!/usr/bin/env python3
"""Defines a module that implements client.GithubOrgClient class"""


import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Defines the class above and implements the test_org method."""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Tests that GithubOrgClient.org returns the correct value"""
        test_payload = {"org_name": org_name}
        github_client = GithubOrgClient(org_name)

        mock_get_json.return_value = test_payload

        result = github_client.org

        mock_get_json.assert_called_once_with(
                f'https://api.github.com/orgs/{org_name}')
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
