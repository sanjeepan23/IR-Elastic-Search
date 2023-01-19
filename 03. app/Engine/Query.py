import json


def basic_search(query):
    return {"query": {"query_string": {"query": query}}}


def search_with_field(query, field):
    return {"query": {"match": {field: query}}}


## Wild Card queries
def wildcard_search(query, field):
    # query is யுக*
    return {"query": {"match": {"field": query}}}


## Multi Match
def multi_match(query, fields=["lyrics", "metaphor"], operator="or"):
    return {
        "query": {
            "multi_match": {
                "query": query,
                "fields": fields,
                "operator": operator,
                "type": "best_fields",
            }
        }
    }


# Multi Match with sorting
def multi_match_with_sorting(
    query, fields=["title", "song_lyrics"], sort_field=None, operator="or"
):
    return {
        "sort": [{sort_field: {"order": "desc"}}],
        "query": {
            "multi_match": {
                "query": query,
                "fields": fields,
                "operator": operator,
                "type": "best_fields",
            }
        },
        "size": 15,
    }


## Bool Queries
def bool_queries(query, field, query2, field2):
    return {
        "query": {
            "bool": {"must": [{"match": {field2: query2}}, {"match": {field: query}}]}
        }
    }


## Aggregate
def agg_multi_match(query, fields=["lyrics", "metaphor"], operator="or"):
    query_code = {
        "size": 500,
        "explain": True,
        "query": {
            "multi_match": {
                "query": query,
                "fields": fields,
                "operator": operator,
                "type": "best_fields",
            }
        },
        "aggs": {
            "Movie Filter": {"terms": {"field": "movie.keyword", "size": 10}},
            "Lyricist Filter": {"terms": {"field": "lyricist.keyword", "size": 10}},
            "Music_director Filter": {
                "terms": {"field": "music_director.keyword", "size": 10}
            },
            "Song Filter": {"terms": {"field": "song.keyword", "size": 10}},
        },
    }

    query_code = json.dumps(query_code)
    return query_code
