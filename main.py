import streamlit as st
import math
from urllib.parse import quote

scale=10
currency="€"


st.title("Linkedin Salary Rank Jobs Finder")

values = st.slider(
    'Select a salary rank in k' + currency,
    0, 300, (55, 200))

exclude = st.text_area(
    "Exclude words (in example company names)",
    "crossover\n"
    "optimus search"
    ).strip()
    
include = st.text_area(
    "Include words (In example technologies)",
    "Kafka\n"
    "AWS"
    ).strip()

minv=values[0]
maxv=values[1]

minm=math.fmod(minv, scale)
maxm=math.fmod(maxv, scale)

#min next
minn=minv+scale-minm
#max bellow
maxb=maxv-maxm

v=minn
filter=""

if minv < minn:
	filter+= "\"" + currency + str(int(minv)) + ",000\" or \"" + currency + str(int(minv)) + "k\""
while v < maxb:
	if len(filter) > 0:
		filter+=" or "
	filter+= "\"" + currency + str(int(v)) + ",000\" or \"" + currency + str(int(v)) + "k\""
	v += scale
if maxb < maxv:
	filter+= "\"" + currency + str(int(maxv)) + ",000\" or \"" + currency + str(int(maxv)) + "k\""
	
filter = "(" + filter + ")"

excludefilter = ""
if len(exclude) > 0:
	for txt in exclude.split("\n"):
		if len(excludefilter) > 0:
			excludefilter+=" or "
		excludefilter += "\"" + txt + "\""
	excludefilter = " and not (" + excludefilter + ")"


includefilter = ""
if len(include) > 0:
	for txt in include.split("\n"):
		if len(includefilter) > 0:
			includefilter+=" and "
		includefilter += "\"" + txt + "\""
	includefilter = " and (" + includefilter + ")"
	
if len(includefilter) > 0:
	filter= "(" +filter + includefilter + ") "
filter+=excludefilter

url = "https://www.linkedin.com/jobs/search/?distance=25&f_TPR=r86400&f_WT=2&geoId=91000000&keywords=" + quote(filter) + "&location=European%20Union&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
st.write (url)

st.link_button("Open in Linkedin", url)


