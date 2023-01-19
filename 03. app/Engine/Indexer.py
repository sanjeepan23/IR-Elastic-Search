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
            "_index": "arrtamil2",
            "_source": {
                "movie": song["திரைப்படம்"],
                "lyricist": song["பாடலாசிரியர்"],
                "music_director": song["இசையமைப்பாளர்"],
                "song": song["பாடல்"],
                "year": song["வருடம்"],
                "lyrics": song["பாடல்வரிகள்"],
                "metaphor": song["உருவகம்"],
                "metaphor_meaning": song["விளக்கம்"],
                "metaphor_type": song["உருவக அணி"],
                "tag": song["குறிச்சொல்"],
            },
        }


songs = read_json("../../data/preprocessed.json")
helpers.bulk(client, convert(songs))
