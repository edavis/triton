import os
import json
import requests

class SourceList(object):
    def __init__(self, path):
        path = os.path.expanduser(path)

        if path.endswith('.json'):
            try:
                resp = requests.get(path, stream=True)
                resp.raise_for_status()
                self.sources = json.load(resp.raw)
            except requests.exceptions.MissingSchema:
                self.sources = json.load(open(path))
        else:
            try:
                resp = requests.get(path)
                resp.raise_for_status()
                self.sources = [url.strip() for url in resp.iter_lines()]
            except requests.exceptions.MissingSchema:
                self.sources = [url.strip() for url in open(path)]
        
    def __iter__(self):
        return iter(self.sources)
