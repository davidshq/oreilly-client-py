import json
import os
from opensearchpy import OpenSearch

host = os.getenv("OS")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
index = os.getenv("INDEX")

client = OpenSearch(
    hosts=[host],
    http_auth=(user, password),
)

# Show the available indices
# indices = client.indices.get_alias().keys()
#print(f"Available indices: {list(indices)}")

# Query for a document by term
query = {
    "size": 1,
    "query": {
        "match": {
            "title": "team"
        }
    }
}
response = client.search(index=index, body=query)
print(json.dumps(response, indent=2))

# Search the index
# response = client.search(index=index, body={"query": {"match_all": {}}})
# print(response)
