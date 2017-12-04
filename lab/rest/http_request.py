"""Example: HTTP Request example"""
import requests

# Set the header
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36 Name',
}

# Execute a request with the GET method
R = requests.get('http://jsonplaceholder.typicode.com/posts', headers=header)
print('# Response Header:\n\t' + str(R.headers))
print('# Response Header - Count:\n\t' + str(len(R.headers)))
print('# Response Header - Get "Date":\n\t' + str(R.headers['Date']))
print('# Status code:\n\t' + str(R.status_code))
print('# Response body (limited):\n\t' + R.text[4:306])