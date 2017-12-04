"""Test: Donwload module"""
# Pre-Condition: install pip packages
# - pytest - execute unit test
# - pytest-html - output html report (e.g.: pytest --html=report.html)
from lab.infra.download import Download
import unittest
import re


class TestDownload(unittest.TestCase):
    """Validate the class Download"""

    def test_download_file(self):
        """
        Validate start download with successful
        """
        # Set the file name
        file_name = 'geckodriver'
        # Set the file version
        file_version = 'v0.19.1'
        # Set the file url
        url_file = 'https://github.com/mozilla/{0}/releases/download/{1}/{0}-{1}-win64.zip'.format(
            file_name, file_version)
        # Validate the method
        download = Download(url_file)
        file_download = download.start()
        file_name = re.search('[\d\w\-\_\.]+\.[a-z]{3,4}$', url_file).group(0)
        self.assertEqual(file_download, file_download)