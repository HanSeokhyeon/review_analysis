import pandas as pd
import streamlit as st
import ssl

from ch4.inference import inference_langchain

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt"
df = pd.read_csv(url, sep='\t')
reviews = st.multiselect("리뷰", df.iloc[:10]['document'])
if st.button("submit"):
    summary = inference_langchain(reviews)
    st.write(summary)
