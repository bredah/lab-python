"""Download drivers for selenium scripts"""
# Pre-Conditions:
# - pip install tqdm - Progress bar

import os
import platform
import requests

from tqdm import tqdm

# Set default vars
download_firefox = true
# Set the driver path
driver_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'driver')
# If not exist the folder, create now
if not os.path.exists(driver_path):
    print('# Create driver folder')
    os.makedirs(driver_path)
# Download drivers
print("# Download driver")
if download_firefox is true:
    if platform.system() == 'Windows':
        print('Hey')


def download_driver(url)
# Start download
    print('Download file from URL: ' + url)
    r = requests.get(url_file, stream=True)
    # Check if the request is successfully
    if r.status_code == 200:
        with open('{0}-{1}-win64.zip'.format(file_name, file_version), 'wb') as f:
            # Using progres sbar
            progressbar = tqdm(
                total=int(int(r.headers['Content-length']) / 1024))
            # Start download
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    progressbar.update()
                    f.write(chunk)
