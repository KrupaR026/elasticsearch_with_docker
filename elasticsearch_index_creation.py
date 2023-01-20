from elasticsearch import Elasticsearch

"""Connect to the Elasticsearch cluster"""

# es = Elasticsearch(['https://localhost:9200'])
es = Elasticsearch()
es = Elasticsearch([{'host': 'localhost', 'scheme':"http", 'port': 9200}])
# es = Elasticsearch(hosts=[{"host": "elasticsearch", 'scheme':"http", "port": 9200}])


"""Define the index settings and mappings"""

settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "id":{"type": "keyword", "index": "true", "store": "true"},
            "first_name": { "type": "text" },
            "last_name": { "type": "text" },
            "age": { "type": "integer" }
        }
    }
}


"""Create the index"""

es.indices.create(index='user_information', body=settings)