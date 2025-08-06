import streamlit as st
import pandas as pd

# set page titie so that it doesnt use my python filename
st.set_page_config(
    page_title="View Dataset",
    page_icon="😢"
)

st.title("View Dataset")   

st.write("""
    This dataset contains a comprehensive set of variables, including temperature, humidity, occupancy levels, HVAC and lighting 
    usage, renewable energy generation, among others. Each record captures a specific moment in time, offering a detailed view of 
    the simulated environment’s conditions. The dataset is constructed to closely resemble energy consumption scenarios that might 
    be encountered in real life, making it valuable for examining the factors that drive energy use. It is well-suited for 
    activities such as exploratory data analysis and the development of predictive models, providing ample opportunity to investigate 
    and understand the various influences on energy consumption.

For more information, visit the source of the dataset at kaggle.
""")

# dataset dir
filePath = "./data/Energy_Consumption_Dataset.csv"

# cache the data
@st.cache_data
def load_csv_data():
    return pd.read_csv(filePath)

# load the data
statistics = load_csv_data()

# set pagination size
PAGE_SIZE = 50

# initialize session state for pagination
if "page_num" not in st.session_state:
    st.session_state.page_num = 0

# calculate total pages
total_pages = (len(statistics) - 1) // PAGE_SIZE + 1

# navigation buttons
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("⬅ Previous", disabled=st.session_state.page_num == 0):
        st.session_state.page_num -= 1
with col3:
    if st.button("Next ➡", disabled=st.session_state.page_num >= total_pages - 1):
        st.session_state.page_num += 1

# calculate slice indices
start_idx = st.session_state.page_num * PAGE_SIZE
end_idx = start_idx + PAGE_SIZE

# display the current page of the dataframe
st.write(f"Showing rows {start_idx + 1} to {min(end_idx, len(statistics))} of {len(statistics)}")
st.dataframe(statistics.iloc[start_idx:end_idx])