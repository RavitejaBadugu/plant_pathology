from fastapi import FastAPI,File
from predict import get_prediction
import numpy as np
import io
from PIL import Image

app=FastAPI()


@app.post('/predict')
async def make_prediction(file: bytes = File(...)):
    img_array=np.asarray(Image.open(io.BytesIO(file)))
    output=get_prediction(img_array)
    return {'data':output}






    