import os
import json
from pprint import pprint


with open(os.environ['GITHUB_EVENT_PATH']) as f:
    data = json.load(f)

pprint(data)
