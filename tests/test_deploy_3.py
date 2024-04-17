import unittest
from unittest.mock import patch
from your_script_name import deploy

class TestDeploy(unittest.TestCase):
    @patch('your_script_name.do_pack')
    @patch('your_script_name.do_deploy')
    def test_deploy_success(self, mock_do_deploy, mock_do_pack):

        mock_do_pack.return_value = 'test_archive_path'

        mock_do_deploy.return_value = True

        result = deploy()

        self.assertTrue(result)
    
    @patch('your_script_name.do_pack')
    @patch('your_script_name.do_deploy')
    def test_deploy_failure(self, mock_do_deploy, mock_do_pack):

        mock_do_pack.return_value = None

        mock_do_deploy.return_value = False

        result = deploy()

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
