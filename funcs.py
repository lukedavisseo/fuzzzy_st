import advertools as adv
import polars as pl
import streamlit as st

# Generates matches based on a sitemap URL input
def generate_matches_from_sitemap(sitemap_url):
	sitemap_df = adv.sitemap_to_df(sitemap_url)
	sitemap_url_list = sitemap_df['loc'].to_list()
	return sitemap_url_list

# Generates matches based on a CSV file input
def generate_matches_from_csv(crawl_csv):
	input_data = pl.read_csv(crawl_csv)
	crawl_csv_url_list = input_data.get_columns()[0].to_list()
	return crawl_csv_url_list

# Generates matches based on a text list input
def generate_matches_from_list(url_list):
	urls_to_check_list = [url for url in url_list.split('\n')]
	return urls_to_check_list

match_generators = {
	'Sitemap': generate_matches_from_sitemap,
	'CSV': generate_matches_from_csv,
	'List': generate_matches_from_list
}

def all_generate_matches(data, input_type):
	match_generator = match_generators.get(input_type)
	if match_generator is None:
		raise ValueError(f"No input type was defined for {input_type}")
	match_list = match_generator(data)
	return match_list

def remove_from_list(list_x, list_y, option):
	set_x = set(list_x)
	set_y = set(list_y)
	if option == 'From List A to List B':
		result_set = set_y - set_x
	else:
		result_set = set_x - set_y
	match_list = list(result_set)

	return match_list