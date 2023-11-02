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

    @patch(
            'client.GithubOrgClient.org',
            new_callable=unittest.mock.PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that the result of _public_repos_url is the expected one based
        on the mocked payload."""
        mock_payload = {
                "repos_url": "https://api.github.com/orgs/testorg/repos"}
        mock_org.return_value = mock_payload

        github_client = GithubOrgClient('testorg')
        result = github_client._public_repos_url

        expected_result = mock_payload["repos_url"]

        self.assertEqual(result, expected_result)

    @patch('client.get_json')
    @patch(
            'client.GithubOrgClient.org',
            new_callable=unittest.mock.PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        expected_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_public_repos_url.return_value =
        "https://api.github.com/orgs/testorg/repos"
        mock_get_json.return_value = expected_payload

        github_client = GithubOrgClient('testorg')
        repos = github_client.public_repos

        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/testorg/repos")

        self.assertEqual(repos, expected_payload)


    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        github_client = GithubOrgClient('testorg')
        result = github_client.has_license(repo, license_key)

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
