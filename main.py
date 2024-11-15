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

"""Show the available indices"""
# indices = client.indices.get_alias().keys()
# print(f"Available indices: {list(indices)}")

"""Get the field mappings for an index"""
# try:
#     mapping = client.indices.get_mapping(index=index)
#     print(json.dumps(mapping, indent=2))
# except Exception as e:
#     print(f"Error getting mapping: {e}")

"""Query for a document by term"""
# query = {
#     "size": 1,
#     "query": {
#         "match": {
#             "title": "team"
#         }
#     }
# }
# response = client.search(index=index, body=query)
# print(json.dumps(response, indent=2))

"""Return all documents"""
# response = client.search(index=index, body={"query": {"match_all": {}}})
# print(response)

"""Add a document to the index"""
document = {
    "title": "TESTOCP: Testing Adding a Document",
    "description": "This is a test document to test adding a document to the index."
}
response = client.index(index=index, body=document)
print(response)
