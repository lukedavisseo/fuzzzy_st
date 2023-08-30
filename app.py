import streamlit as st
import pandas as pd
import floutils as flou

st.header("Welcome to Flou!")

st.info("Flou is a fuzzy matching tool designed to match strings from a given dataset to aid a variety of content and technical SEO tasks such as redirect mapping and internal linking opportunities.")

data = st.file_uploader(
    "1 - Upload a CSV with at least one column containing the strings you want to match.",
    type=["csv", "xls"],
    accept_multiple_files=False,
)

if data:
    df = pd.read_csv(data)
    string_column = st.selectbox("2 - Select the column you want to use for matching", df.columns)
    primary_strings_list = df[string_column].to_list()
    strings_to_match = st.text_area(
        "3 - Now enter the titles/URLs/strings you want to match with that list."
    )
    generate = st.button("Generate")

    if generate and __name__ == "__main__":
        try:
            secondary_strings_list = strings_to_match.split("\n")
            from_list = [primary_string for primary_string in primary_strings_list]
            to_list = [secondary_string for secondary_string in secondary_strings_list]
            df_1 = flou.get_tf_idf_results(from_list, to_list)
            df_2 = flou.get_all_minilm_l6_v2_results(from_list, to_list)
            df_3 = flou.all_mpnet_base_v2(from_list, to_list)
            df_final = flou.display_all_dfs(df_1, df_2, df_3)
            st.dataframe(df_final)
            flou_csv = df_final.to_csv(index=False)
            st.download_button(
                label="Download as CSV",
                data=flou_csv,
                file_name="fuzzy_matched_titles.csv",
            )
        except Exception as error:
            if type(error) in flou.errors_dict:
                st.warning(flou.errors_dict[type(error)])
