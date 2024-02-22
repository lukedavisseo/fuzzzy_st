# Fuzzzy ST
 A fuzzy matching tool

## Intro
Fuzzzy ST is a fuzzy matching tool designed to match strings from a given dataset to aid a variety of content and technical SEO tasks. It will use fuzzy matching libraries and Python to do this.

## Quick instructions

1. Choose one of the modes in the left sidebar: Sitemap, CSV, and List
 1a. If you choose Sitemap, enter the sitemap URL in the first text input field
 1b. If you choose CSV, upload a CSV of the strings you want to match. You can then pick the column you want to use to match.
 1c. If you choose List, you can add a list of strings (e.g. URLs, titles, headings), one per line
3. Create a CSV with at least one column of strings (URLs, titles, headings)
4. Under List B, add your second list of strings, one per line
5. Now, you need to decide which way you want to match your lists. "I want to find which URLs from List B match with URLs in List A" will make List A the "master" list and "I want to find which URLs from List A match with URLs in List B" will make List B the "master" list. This might be confusing, and it is to me too so if you need help, ask me!
6. Once everything is ready, click Submit and you will get a table of both lists in two columns (From and To) and their similarity score in the final column (100% means a perfect match and anything closer to 0% means a poor match). 
9. You can download this table as a CSV if you click on the download icon in the top right corner.

## Data input
Fuzzzy ST accepts text data in three formats (via a sitemap URL, a CSV file, or manually inputted strings). That text data can be any of the following (but not exclusively):

* URLs
* Metadata (meta titles and meta descriptions)
* Headings (H1-H6)

## Processing
Fuzzzy ST uses PolyFuzz, a fuzzy matching Python package, to determine matching scores for two given datasets. The algorithm is [TF-IDF](https://maartengr.github.io/PolyFuzz/api/models/tfidf/) but there are different models available.

The original plan was to use 3 different models and get an average score but, honestly, that felt like overkill for our use cases.

## Benefits for SEO department

The main function of this tool will be to help SEOs with their optimisation tasks in the following ways:

### Redirect maps

Redirect maps can be challenging for larger sites but with a fuzzy matching tool, the time taken to find matches would be drastically reduced. An example of this is with XLC where we were tasked to create redirect maps for 4 different languages (English, German, Dutch, and French). There was naturally a language barrier but fuzzy matching helped significantly; we may not have completed the text without it. Approximately 50% of the URLs matched had match scores above 75% which were confirmed to be correct and this was using only one model (TF-IDF).

### Internal linking

There are a variety of ways to find internal linking opportunities but some of the easiest is pages with similar titles or URLs, and that’s where fuzzy matching comes in handy. Taking a list of pages with low URL Rank and comparing them to the rest of a site’s URLs can show opportunities where similar pages aren’t linked. You can also do this with titles/H1s and this works especially well with sites that have uniform titles or headings.

An example of this use is with FireSealsDirect and The Access Group. This process was in conjunction with a graph science tool which found missing link pairs that had a common link pair between them (ie. Page A and Page B linked to Page C but not each other). After identifying these missing pairs, I ran a fuzzy matching search on the remaining pages’ titles and found areas of opportunity. The most common pairs were related products which suggested a need for a related products module, for example.

## Performance considerations

Because TF-IDF is a simple algorithm, the speed of generating matches is dependent on the number of strings you want to compare. Accuracy is also dependent on the strings you're comparing. Ideally, both lists should be similar in nature (URLs vs URLs, titles vs. titles). You should also keep in mind that this algorithm will not check for semantic similarity, so "**cat**" and "**cat**astrophy" may have a closer score than "cat" and "kitten".
