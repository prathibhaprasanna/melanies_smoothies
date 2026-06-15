import streamlit as st
import pandas as pd
from snowflake.snowpark.functions import col
import requests

st.title("Smoothie App - Debug Mode")

cnx = st.connection('snowflake')
session = cnx.session()

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'), col('SEARCH_ON'))
pd_df = my_dataframe.to_pandas()

st.write("Columns in DataFrame:", pd_df.columns.tolist())
st.write("First 5 rows:")
st.dataframe(pd_df.head()))

