"""Example: Script to download a file"""
# Pre-Conditions:
# - pip install tqdm - Progress bar
import requests
import re
from tqdm import tqdm


class Download:

    def __init__(self, url):
        self.url = url

    def start(self):
        '''
        Download a file from the url
        :return: File name
        '''
        file_name = ""
        try:
            file_name = re.search(
                '[\d\w\-\_\.]+\.[a-z]{3,4}$', self.url).group(0)
        except AttributeError:
            raise Exception('Not possible to download the URL file')
        # Start download
        print('Download file from URL: ' + self.url)
        r = requests.get(self.url, stream=True)
        # Check if the request is successfully
        if r.status_code == 200:
            with open(file_name, 'wb') as f:
                # Using progress bar
                progressbar = tqdm(
                    total=int(int(r.headers['Content-length']) / 1024))
                # Start download
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        progressbar.update()
                        f.write(chunk)
        return file_name