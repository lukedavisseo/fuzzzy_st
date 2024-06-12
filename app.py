import advertools as adv
from polyfuzz import PolyFuzz
import pandas as pd
import streamlit as st

# Generates matches based on a sitemap URL input
def generate_matches_from_sitemap(sitemap_url):
	sitemap_df = adv.sitemap_to_df(sitemap_url)
	sitemap_url_list = sitemap_df['loc'].to_list()
	return sitemap_url_list

# Generates matches based on a CSV file input
def generate_matches_from_csv(crawl_csv, column_name):
	crawl_csv_url_list = data[column_name].tolist()
	return crawl_csv_url_list

# Generates matches based on a text list input
def generate_matches_from_list(url_list):
	urls_to_check_list = [url for url in url_list.split('\n')]
	return urls_to_check_list

# Titles and stuff
st.header('Fuzzzy ST')
st.info('Fuzzzy ST is a fuzzy matching tool designed to match strings from a pair of datasets to aid a variety of content and technical SEO tasks. It uses a fuzzy matching algorithm (TF-IDF) to do this and dramatically reduces the time taken to generate things like redirect maps.', icon=None)

with st.expander("A quick how-to"):
    st.write('''
        1. Select one of the input types on the left to obtain your first set of URLs or strings.
        2. Once selected, enter your sitemap URL/upload your CSV/add your list under List A
        3. Add your second list under List B
        4. Pick whether you want to match from List A to List B or List B to List A. (Click the "I'm confused by the List A/B thing!" expander for some examples.)
        5. Click Generate to generate your matches
        6. Click the Download icon to downlad the matches as a CSV file. You can also expand the table to see it in full screen.
    ''')

with st.expander("I'm confused by the List A/B thing!"):
	st.write('''
    	- For redirects, the direction depends on which list (A or B) has the old site URLs and the new site URLs as you're going from "old to new".

    		- If List A has the old URLs and List B has the new URLs, it's List A -> List B.
    		- If List B has the old URLs and List A has the new URLs, it's List B -> List A.

    	- For something like matching a long list of keywords variations to a short list of "master" keywords, you're going from "long to short".

    		- If List A has the long list and List B has the short list, it's List A -> List B.
    		- If List B has the long list and List A has the short list, it's List B -> List A.

    	If you're still unsure, send me a message and we can figure it out together!
    ''')

st.subheader("List A")

input_type = st.sidebar.radio("Choose an input type", ['Sitemap', 'CSV', 'List'])

if input_type == 'Sitemap':
	sitemap_url = st.text_input("Enter the sitemap URL")
elif input_type == 'CSV':
	crawl_csv = st.file_uploader('Or upload your CSV file. Make sure the URL column is called "URLs"', type="csv")
	if crawl_csv:
		data = pd.read_csv(crawl_csv)
		st.dataframe(data)
		column_options = st.radio('Choose the column you want to fuzzy match', data.columns.to_list())
elif input_type == 'List':
	url_list = st.text_area('Or add a list of URLs to check, 1 per line')

st.subheader("List B")

list_b = st.text_area('Now, add the list of URLs or strings you want to match with it.')

option_picker = st.radio("Which way do you want to match the lists?", ['From List A to List B', 'From List B to List A'])

generate = st.button("Generate")

if generate:

	test_list = [url for url in list_b.split('\n')]

	if input_type == 'Sitemap':
		match_list = generate_matches_from_sitemap(sitemap_url)
	elif input_type == 'CSV':
		match_list = generate_matches_from_csv(crawl_csv, column_options)
	else:
		match_list = generate_matches_from_list(url_list)

	if option_picker == 'From List A to List B':
		model = PolyFuzz().match(match_list, test_list)
	else:
		model = PolyFuzz().match(test_list, match_list)

	# This converts the matches into another DataFrame
	df = model.get_matches()

	# Display DataFrame
	st.dataframe(df)
