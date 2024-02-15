import advertools as adv
from polyfuzz import PolyFuzz
import pandas as pd
import streamlit as st

def generate_matches_from_sitemap(sitemap_url):
	sitemap_df = adv.sitemap_to_df(sitemap_url)
	sitemap_url_list = sitemap_df['loc'].to_list()
	return sitemap_url_list

def generate_matches_from_csv(crawl_csv, column_name):
	crawl_csv_url_list = data[column_name].tolist()
	return crawl_csv_url_list

def generate_matches_from_list(url_list):
	urls_to_check_list = [url for url in url_list.split('\n')]
	return urls_to_check_list

st.header('Fuzzzy ST')
st.subheader("List A")

input_type = st.sidebar.radio("Choose an input type", ['Sitemap', 'CSV', 'List'])

if input_type == 'Sitemap':
	sitemap_url = st.text_input("Enter the sitemap URL")
elif input_type == 'CSV':
	crawl_csv = st.file_uploader('Or upload your CSV file. Make sure the URL column is called "URLs"', type="csv")
	if crawl_csv:
		data = pd.read_csv(crawl_csv)
		column_options = st.radio('Choose the column you want to fuzzy match', data.columns.to_list())
elif input_type == 'List':
	url_list = st.text_area('Or add a list of URLs to check, 1 per line')

st.subheader("List B")

list_b = st.text_area('Now, add the list of URLs you want to match with it.')

option_picker = st.radio("Which way do you want to match the URL lists?", ['I want to find which URLs from List B match with URLs in List A', 'I want to find which URLs from List A match with URLs in List B'])

submit = st.button("Submit")

if submit:

	test_list = [url for url in list_b.split('\n')]

	if input_type == 'Sitemap':
		match_list = generate_matches_from_sitemap(sitemap_url)
	elif input_type == 'CSV':
		match_list = generate_matches_from_csv(crawl_csv, column_options)
	else:
		match_list = generate_matches_from_list(url_list)

	if option_picker == 'I want to find which URLs from List B match with URLs in List A':
		model = PolyFuzz().match(match_list, test_list)
	else:
		model = PolyFuzz().match(test_list, match_list)

	# This converts the matches into another DataFrame
	df = model.get_matches()

	# Display DataFrame
	st.dataframe(df)
