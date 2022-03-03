import urllib.request # for pulling images
import urllib.parse
import os



# filename = 'university_of_hawai_manoa_logo.jpg'
# myPath = 'logos/'
# fullfilename = os.path.join(myPath, filename)

# image_url ='https://yocket.com/_ipx/f_webp,q_100/https://static.yocket.in/images/universities/logos/university_of_hawai_manoa_logo.jpg'

# urllib.request.urlretrieve(image_url, fullfilename)


#code for json data

import json
 
# Opening JSON file
f = open('us_colleges.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
myPath = 'logos/'


# Iterating through the json
# list
# setting ranges for better results and debugging
# it start from zero to last length or json file
for i in range(963, len(data['result'])):
	#  string file name in json
	file =data['result'][i]['logo_url']

	#cheking file sting type non or alternative logo accordinf to this data
	if(file != None and file != 'alt_university_logo.png' and (file.isascii())):
		# file extenstion  checks
		if(file.lower().endswith(('.png', '.jpg', '.jpeg'))):
			# just prinint stuf 
			print(data['result'][i]['logo_url']+ 'downloaded file no',i)
			# storing exact filename
			# fname = data['result'][i]['logo_url']
			filename = data['result'][i]['logo_url']

			#full filename and path joining
			fullfilename = os.path.join(myPath, filename)

			#image url directory from yocket

			image_url ='https://yocket.com/_ipx/f_webp,q_100/https://static.yocket.in/images/universities/logos/'+filename
			#decoding url sting 
			print(image_url)
			uncoded_url = urllib.parse.unquote(image_url)
			#saving fucking images 
			urllib.request.urlretrieve(uncoded_url, fullfilename) 
		else:
			print('fucked at image', i)
 
# Closing file
f.close()