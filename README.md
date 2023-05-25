# A Search Engine: Top Tamil melody songs Composed by A.R.Rahman from the years 2000 to 2010



## Overview

This report details the process of constructing a text corpus and search application utilizing
Elasticsearch, including data scraping, cleaning, indexing, text processing, and the creation
of a web interface for testing the application.

Fig-1: Overview of the System

## Steps

1. Scraping Lyrics and metadata

The corpus data was obtained by scraping allnewlyrics.com using Scrapy and
Python. The process began by using the main spider to gather URLs of movie pages,
then the sub-spider visited those URLs to scrape movie lyrics and additional
information. Once the site was scraped, the data was saved in HTML files and
BeautifulSoup was utilized to extract the information from the stored HTML files.

2. Annotate Metaphors

After gathering the information, every single one of the 100 songs was carefully
labeled with the metaphors present and their interpretations. Furthermore, different
types of metaphors and labels for metaphors were also labeled in order to build up
the collection.




3. Preprocessing & Re-structuring

Initially, every word in the English language was substituted with its corresponding Tamil equivalent (A.R.Rahman → ஏ ஆꢀ ரꢁமாꢂ). Secondly, the lyrics were altered to remove multiple newline characters and other characters to enhance the search functionality. Lastly, the data was rearranged into a JSON format for easy
indexing.

Fig-2: JSON Format of the Corpus

4\. Indexing & Text Processing

Manual enhancements were made to the indexing process by incorporating tools
such as stemmer, stopwords, and synonyms into the custom analyzer. Once these
custom analyzers were added, the indexed function was executed to generate an
index for the corpus.

5\. Basic and Advance Queries

After indexing, multiple queries were implemented using Query DSL via Python.
Which includes the following types of queries:

● Simple Search Query

● Search with Field Query
● Wildcard Query

● MultiMatch Query

● MultiMatch with Sorting Query
● Bool Query

● Aggregated Multimatch Query

● Aggregated MultiMatch with Sorting Query




<a name="br3"></a>6. Web UI

In conclusion, a web-based user interface utilizing H2O-Wave and Python was created to
evaluate and showcase the system's capabilities. This interface features various functions
such as Basic Search, Multi-Match, and Aggregated MultiMatch with sorting capabilities.

Fig-3: MultiMatch Input

Fig-4: Output of ES

Supported Queries
## Basic
அன்பே

## Multi match
அன்பே
movie
lyricist


# Agg
அன்பே
movie
song
