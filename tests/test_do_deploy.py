import unittest
from unittest.mock import patch
from fabric.api import env
from fabric.operations import put, run
from your_script_name import do_deploy

class TestDoDeploy(unittest.TestCase):
    @patch('fabric.operations.put')
    @patch('fabric.operations.run')
    def test_do_deploy_success(self, mock_run, mock_put):

        env.hosts = ['test_server']

        mock_put.return_value.succeeded = True

        mock_run.return_value.succeeded = True

        result = do_deploy('test_archive_path')
        self.assertTrue(result)
    
    @patch('fabric.operations.put')
    @patch('fabric.operations.run')
    def test_do_deploy_failure(self, mock_run, mock_put):

        env.hosts = ['test_server']

        mock_put.return_value.succeeded = True

        mock_run.return_value.succeeded = False

        result = do_deploy('test_archive_path')

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
