import streamlit as st
from polyfuzz import PolyFuzz
from polyfuzz.models import SentenceEmbeddings

errors_dict = {
    TypeError: "Looks like there might have been an unexpected typing error. Check the file and try again. (TypeError)",
    ValueError: "Have you submitted a file or is it empty? (ValueError)",
}


@st.cache_resource
def get_tf_idf_results(from_list, to_list):
    model_tf_idf = PolyFuzz("TF-IDF").match(from_list, to_list)
    df_tf_idf = model_tf_idf.get_matches()
    df_tf_idf = df_tf_idf[
        (df_tf_idf["Similarity"] > 0.0) & (df_tf_idf["Similarity"] < 0.98)
    ].sort_values(["Similarity"], ascending=False)

    return df_tf_idf


@st.cache_resource
def get_all_minilm_l6_v2_results(from_list, to_list):
    distance_model = SentenceEmbeddings("all-MiniLM-L6-v2")
    model_data = PolyFuzz(distance_model).match(from_list, to_list)
    df_minilm = model_data.get_matches()
    df_minilm = df_minilm[
        (df_minilm["Similarity"] > 0.0) & (df_minilm["Similarity"] < 0.98)
    ].sort_values(["Similarity"], ascending=False)

    return df_minilm


@st.cache_resource
def all_mpnet_base_v2(from_list, to_list):
    distance_model = SentenceEmbeddings("all-mpnet-base-v2")
    model_data = PolyFuzz(distance_model).match(from_list, to_list)
    df_mpnet = model_data.get_matches()
    df_mpnet = df_mpnet[
        (df_mpnet["Similarity"] > 0.0) & (df_mpnet["Similarity"] < 0.98)
    ].sort_values(["Similarity"], ascending=False)

    return df_mpnet


@st.cache_resource
def display_all_dfs(df_1, df_2, df_3):
    df_final = df_1
    df_final.rename(columns={"Similarity": "TF-IDF"}, inplace=True)
    df_final["MiniLM"] = df_2["Similarity"]
    df_final["mpnet"] = df_3["Similarity"]
    df_final["Avg. score"] = (
        df_final[["TF-IDF", "MiniLM", "mpnet"]].mean(axis=1).round(3)
    )
    df_final = df_final[df_final["TF-IDF"] > 0.000].sort_values(
        ["Avg. score"], ascending=False
    )

    return df_final
