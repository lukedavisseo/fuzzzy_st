# Flou
 A fuzzy matching tool

## Intro
Flou is a fuzzy matching tool designed to match strings from a given dataset to aid a variety of content and technical SEO tasks. It will use fuzzy matching libraries and Python to do this.

## Quick instructions

1. Create a CSV with at least one column of strings (URLs, titles, headings)
2. Upload that CSV to Flou
3. Select the column you want to use for matching
4. Enter a list of strings you want to match against the list from your CSV
5. Click Generate
6. A table will pop up and display the matches and their average matching scores
7. Click Download CSV to download the table in a CSV file

## Data input
Currently, Flou will only accept text data from CSV files. That text data can be any of the following (but not exclusively):

* URLs
* Metadata (meta titles and meta descriptions)
* Headings (H1-H6)

## Processing
Flou uses PolyFuzz, a fuzzy matching Python package, to determine matching scores for two given datasets with help from three language models:

* TF-IDF
* all-MiniLM-L6-v2
* all-mpnet-base-v2

The reason for using 3 models rather than 1 is because they each come with their own strengths and weaknesses in matching certain texts. In tests, I’ve found that TF-IDF works well with comparing strings that are very similar (“cats” vs. “cat”), but not if the similarity is only semantic (“cats” vs. “kittens”).

## Benefits for SEO department

The main function of this tool will be to help SEOs with their optimisation tasks in the following ways:

### Redirect maps

Redirect maps can be challenging for larger sites but with a fuzzy matching tool, the time taken to find matches would be drastically reduced. An example of this is with XLC where we were tasked to create redirect maps for 4 different languages (English, German, Dutch, and French). There was naturally a language barrier but fuzzy matching helped significantly; we may not have completed the text without it. Approximately 50% of the URLs matched had match scores above 75% which were confirmed to be correct and this was using only one model (TF-IDF).

### Internal linking

There are a variety of ways to find internal linking opportunities but some of the easiest is pages with similar titles or URLs, and that’s where fuzzy matching comes in handy. Taking a list of pages with low URL Rank and comparing them to the rest of a site’s URLs can show opportunities where similar pages aren’t linked. You can also do this with titles/H1s and this works especially well with sites that have uniform titles or headings.

An example of this use is with FireSealsDirect and The Access Group. This process was in conjunction with a graph science tool which found missing link pairs that had a common link pair between them (ie. Page A and Page B linked to Page C but not each other). After identifying these missing pairs, I ran a fuzzy matching search on the remaining pages’ titles and found areas of opportunity. The most common pairs were related products which suggested a need for a related products module, for example.

## Performance considerations

Due to the size of the language models, it may take a while to run the tool for large datasets. This could be mitigated by allowing the user to select the models they want to use rather than using all three by default. This may be at the expense of quality but the results would be quicker.