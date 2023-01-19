{
    "settings": {
        "analysis": {
            "analyzer": {
                "my_custom_analyzer": {
                    "tokenizer": "standard",
                    "filter": ["cus_stemmer", "cus_stopwords", "cus_synonyms"],
                }
            },
            "filter": {
                "cus_stemmer": {
                    "type": "stemmer_override",
                    "rules_path": "03. app/Analyzer/stemmer.txt",
                },
                "cus_stemmer": {
                    "type": "stop",
                    "stopwords_path": "03. app/Analyzer/stopwords.txt",
                },
                "cus_stemmer": {
                    "type": "synonym",
                    "stopwords_path": "03. app/Analyzer/synonym.txt",
                },
            },
        }
    }
}
