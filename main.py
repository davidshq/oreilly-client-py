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


def get_available_indices():
    """Show the available indices"""
    indices = client.indices.get_alias().keys()
    print(f"Available indices: {list(indices)}")


def get_field_mappings():
    """Get the field mappings for an index"""
    mapping = client.indices.get_mapping(index=index)
    print(json.dumps(mapping, indent=2))


def get_document_by_id():
    """Get a document by ID"""
    doc_id = "1"
    response = client.get(index=index, id=doc_id)
    print(json.dumps(response['_source'], indent=2))


def get_document_by_query():
    """Query for a document by term"""
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


def get_all_documents():
    """Get all documents"""
    response = client.search(index=index, body={"query": {"match_all": {}}})
    print(response)


def add_document():
    """Add a document to the index"""
    document = {
        "title": "TESTOCP: Testing Adding a Document",
        "description": "This is a test document to test adding a document to the index."
    }
    response = client.index(index=index, body=document)
    print(response)


def delete_document_by_id():
    """Delete a document from the index by ID"""
    doc_id = "1"
    response = client.delete(
        index=index,
        id=doc_id,
        params={"refresh": "true"}
    )
    print(response)


def delete_document_by_query():
    """Delete a document from the index by query"""
    delete_query = {
        "query": {
            "match": {
                "title": "TESTOCP"
            }
        }
    }
    response = client.delete_by_query(
        index=index,
        body=delete_query,
        params={"refresh": "true"}
    )
    print(response)
