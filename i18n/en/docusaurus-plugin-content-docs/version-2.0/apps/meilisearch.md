---
title: Meilisearch
slug: /meilisearch
tags:
  - Fuzzy search 
  - Real-time Indexing 
  - Meilisearch
---

import Meta from './_include/meilisearch.md';

<Meta name="meta" />

## Getting started{#guide}

### Add Index 

1. After installing Meilisearch on the Websoft9 console, view the application details through **My Applications** and obtain the access URL in the **Access** tab 

2. The browser accesses the URL and currently has no Index 

3. Use the following command to send an index data 
    ``` 
    curl \ 
    -X POST ' http://IP:Port/indexes/movies/documents ' \ 
    -H 'Content-Type: application/json' \ 
    --data-binary '[ 
    { "id": 1, "title": "Justice League", "genre": ["Action", "Adventure"] }, 
    { "id": 2, "title": "Wonder Woman", "genre": ["Action", "Fantasy"] }, 
    { "id": 3, "title": "The Avengers", "genre": ["Action", "Sci-Fi"] }, 
    { "id": 4, "title": "Inception", "genre": ["Action", "Sci-Fi", "Thriller"] }, 
    { "id": 5, "title": "The Dark Knight", "genre": ["Action", "Crime", "Drama"] } 
    ]' 
    ``` 

4. Returning to the page again, the index data can be displayed normally

## Configuration options{#configs}

## Administer{#administrator}

## Troubleshooting{#troubleshooting}