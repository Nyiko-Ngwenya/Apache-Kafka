from elasticsearch import Elasticsearch
from secrets import main_host,username,password,host

es = Elasticsearch(hosts=[host])
# es = Elasticsearch(
#     [main_host],
#     http_auth=(username, password),
#     scheme="https",
#     port=port,
# )

es.indices.create(index="twitter")

# es.create(index="twitter",id=2,body={"random":2},doc_type="tweets")