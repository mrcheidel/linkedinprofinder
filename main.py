import streamlit as st
from linkedin import gen_filter

st.set_page_config(page_title="Linkedin Job Finder: Filter Helper", page_icon="shark")
st.title("Linkedin Job Finder: Filter Helper")

placetowork = st.multiselect(
    'Place to work',
    ['Remote', 'Hybrid', 'On-Site'],
    ['Remote'])

values = st.slider(
    'Select a salary rank in k',
    40, 250, (100, 250))
    

exclude = st.text_area(
    "Exclude words (in example company names)",
    "crossover\n"
    "optimus search"
    ).strip()
    
include = st.text_area(
    "Include words in the Job Title",
    ""
    ).strip()
  
with st.expander("ADVANCED"):
	pattern = st.text_input(
        "Salary pattern",
        value="\"{salary},000\" OR \"{salary}k\""
    ).strip()
    
	geoId = st.text_input(
        "GeoId:",
        value="91000007"
    ).strip()
    
	location = st.text_input(
        "Location:",
        value="EMEA"
    ).strip()
    
	url = gen_filter(values, exclude, include, 10, placetowork, pattern, location, geoId)
	st.write (url)
	st.write ("Contact: [Linkedin](https://www.linkedin.com/in/mrcheidel/)")
	
st.link_button("Apply on Linkedin", url)
