import streamlit as st
from linkedin import gen_filter

st.set_page_config(page_title="Linkedin Salary Rank Jobs Finder", page_icon="shark")
st.title("Linkedin Salary Rank Jobs Finder")

placetowork = st.multiselect(
    'Place to work',
    ['Remote', 'Hybrid', 'On-Site'],
    ['Remote'])

values = st.slider(
    'Select a salary rank in k',
    0, 300, (100, 250))
    
    
pattern="\"{salary},000\" OR \"{salary}k\""
pattern = st.text_input(
        "Enter the salary pattern here 👇",
        value=pattern
    ).strip()

exclude = st.text_area(
    "Exclude words (in example company names)",
    "crossover\n"
    "optimus search"
    ).strip()
    
include = st.text_area(
    "Include words in the Job Title",
    ""
    ).strip()
	
url = gen_filter(values, exclude, include, 10, placetowork, pattern)
st.write (url)
st.link_button("Open in Linkedin", url)
st.write (":link: [gihub](https://github.com/mrcheidel/linkedinprofinder)")
