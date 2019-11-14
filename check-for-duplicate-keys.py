#!/usr/bin/env python3
import json
import urllib.parse
import urllib.request

def main():
    AUTH_TOKEN='<set>'
    BASE_URL='http://localhost:8000/api/v1/issues/?application=8&order=date_updated&page_size=100'
    url = BASE_URL + "&page=1"
    ids = []
    while True:
        req = urllib.request.Request(url)
        req.add_header('Authorization', 'Token ' + AUTH_TOKEN)
        req.add_header('Content-Type', 'application/json')
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36')
        with urllib.request.urlopen(req) as f:
            json_data = json.loads(f.read().decode('utf-8'))
            for item in json_data['results']:
                if (item['id'] in ids):
                    print("Conflict found.")
                    exit(1)
                else:
                    ids.append(item['id'])
            if json_data['next']:
                url = json_data['next']
            else:
                break
    print("list item count: " + str(len(ids)))
    print("set item count: " + str(len(set(ids))))
main()