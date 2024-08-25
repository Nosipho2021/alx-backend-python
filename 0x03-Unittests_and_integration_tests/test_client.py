#!/usr/bin/env python3
""" Module for testing the client """

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, PropertyMock

class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing GithubOrgClient """

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        client.org
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')

    def test_public_repos_url(self):
        """Test that the result of _public_repos_url is the expected one"""
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            payload = {"repos_url": "World"}
            mock_org.return_value = payload
            client = GithubOrgClient('test')
            result = client._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that the list of repos is what you expect from the chosen payload"""
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_get_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "hello/world"
            client = GithubOrgClient('test')
            result = client.public_repos()
            expected_result = [repo["name"] for repo in json_payload]
            self.assertEqual(result, expected_result)

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Unit-test for GithubOrgClient.has_license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)

@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Class for integration tests using fixtures"""

    @classmethod
    def setUpClass(cls):
        """Set up the class with mocks for requests.get"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url, *args, **kwargs):
            """Side effect function for mocking responses"""
            if url.endswith('/orgs/google'):
                return unittest.mock.Mock(json=lambda: cls.org_payload)
            elif url.endswith('/orgs/google/repos'):
                return unittest.mock.Mock(json=lambda: cls.repos_payload)
            elif url.endswith('/orgs/apache2/repos'):
                return unittest.mock.Mock(json=lambda: cls.apache2_repos)
            raise ValueError(f'Unexpected URL: {url}')

        cls.mock_get.side_effect = side_effect

    def test_public_repos(self):
        """Integration test for public_repos"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.mock_get.assert_called()

    def test_public_repos_with_license(self):
        """Integration test for public_repos with license"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
        self.mock_get.assert_called()

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher after tests"""
        cls.get_patcher.stop()
