import os
import streamlit as st
import requests

api_key=st.secrets["NASA_API_KEY"]
#os.environ.get("NASA_API_KEY")
url=f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

resp=requests.get(url)
content=resp.json()

title=content['title']
date=content['date']
img_url=content['url']
explanation=content['explanation']

#
img_file='image.jpg'
def get_image():
    resp_img=requests.get(img_url)
    #print(resp_img.content)
    with open(img_file,'wb') as file:
        file.write(resp_img.content)

get_image()
st.title(title)
st.subheader(date)
st.image(img_file)
st.write(explanation)
