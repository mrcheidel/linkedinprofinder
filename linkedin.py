import math
from urllib.parse import quote

def gen_filter(values, exclude, include, scale, placetowork, pattern):
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
	print("0")
	if minv < minn:
		filter+=pattern.replace("{salary}", str(int(minv)))
	while v < maxb:
		if len(filter) > 0:
			filter+=" OR "
		filter+=pattern.replace("{salary}", str(int(v)))
		v += scale
	if maxb < maxv:
		if len(filter) > 0:
			filter+=" OR "
		filter+=pattern.replace("{salary}", str(int(maxv)))
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
