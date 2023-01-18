from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json, re
import codecs
import unicodedata

client = Elasticsearch(HOST="http://localhost", PORT=9200)
INDEX = "lyrics"


def read_json(path):
    with open(path, "r", encoding="utf-8-sig") as f:
        json_data = json.load(f)
    return json_data["data"]


def convert(songs):
    for song in songs:
        yield {
            "_index": "arrtamil",
            "_source": song,
        }


songs = read_json("../data/preprocessed.json")
helpers.bulk(client, convert(songs))
