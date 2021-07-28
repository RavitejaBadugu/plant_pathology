import streamlit as st
import requests
import pickle
import os
from requests_toolbelt.multipart.encoder import MultipartEncoder


def process(image, server_url: str):

    m = MultipartEncoder(fields={"file": ("filename", image, "image/jpeg")})

    r = requests.post(
        server_url, data=m, headers={"Content-Type": m.content_type}, timeout=8000
    )

    return r

def app():
    st.title('Below please upload the image to get predictions')
    image_file=st.file_uploader('upload image',type=['.jpg','.png'],accept_multiple_files=False)
    if image_file is not None:
        with st.spinner(text='In progress'):
            response=process(image_file,'http://localhost:8000/predict')
            final=response.json()['data']
            if type(final)=='int':
                st.success(f"uploaded image belongs to {final}")
            else:
                st.warning(final)