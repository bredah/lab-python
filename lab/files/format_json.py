"""Example: JSON parser"""
import json
import requests

# Set the header
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36 Name',
}

# Execute a request with the GET method
R = requests.get('http://jsonplaceholder.typicode.com/posts', headers=header)

# JSON Parser
J = json.loads(R.text)
print('# JSON Parser - Position 01\n\t' + str(J[0]['userId']) + '>>' + str(J[0]['id']) +
      '>>' + J[0]['title'][:15] + '>>' + J[0]['body'][:10])
print('# JSON Parser - Position 02\n\t' + str(J[1]['userId']) + '>>' + str(J[1]['id']) +
      '>>' + J[1]['title'][:15] + '>>' + J[1]['body'][:10])