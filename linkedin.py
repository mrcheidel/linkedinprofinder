import math
from urllib.parse import quote

def gen_filter(values, exclude, include, scale, currency, placetowork):
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
		filter+= "\"" + currency + str(int(minv)) + ",000\" OR \"" + currency + str(int(minv)) + "k\""
	while v < maxb:
		if len(filter) > 0:
			filter+=" OR "
		filter+= "\"" + currency + str(int(v)) + ",000\" OR \"" + currency + str(int(v)) + "k\""
		v += scale
	if maxb < maxv:
		filter+= "\"" + currency + str(int(maxv)) + ",000\" OR \"" + currency + str(int(maxv)) + "k\""
	
	filter = "(" + filter + ")"

	excludefilter = ""
	if len(exclude) > 0:
		for txt in exclude.split("\n"):
			if len(excludefilter) > 0:
				excludefilter+=" OR "
			excludefilter += "\"" + txt + "\""
		excludefilter = " AND NOT (" + excludefilter + ")"


	includefilter = ""
	if len(include) > 0:
		for txt in include.split("\n"):
			if len(includefilter) > 0:
				includefilter+=" OR "
			includefilter += "\"" + txt + "\""
		includefilter = " AND (" + includefilter + ")"
	
	if len(includefilter) > 0:
		filter= "(" +filter + includefilter + ") "
	filter+=excludefilter

	f_WT=""
	if "Remote" in placetowork:
		if len(f_WT)>0:
			f_WT+=","
		f_WT+="2"

	if "Hybrid" in placetowork:
		if len(f_WT)>0:
			f_WT+=","
		f_WT+="3"
	if "On-Site" in placetowork:
		if len(f_WT)>0:
			f_WT+=","
		f_WT+="1"

	url = "https://www.linkedin.com/jobs/search/?distance=25&f_TPR=r604800"
	if len(f_WT)>0:
		url += "&f_WT=" + quote(f_WT)
	url += "&geoId=91000000&keywords=" + quote(filter) + "&location=European%20Union&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
	return (url)