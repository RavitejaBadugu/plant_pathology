from fastapi import FastAPI,File,UploadFile
from predict import get_prediction
import os
import shutil
import uvicorn
app=FastAPI()


@app.get('/')
async def wel_fn():
    return {'message': 'welcome to this api. In url go to /docs to try it out'}

@app.post('/predict')
async def make_prediction(file: UploadFile = File(...)):
    try:
        image_type=file.filename.split('.')[-1]
        if image_type in ['jpg','png']:
            image_path=f'tmp/temp_image.{image_type}'
            with open(image_path, 'wb') as f:
                shutil.copyfileobj(file.file, f)
            output=get_prediction(image_path)
            os.remove(image_path)
            return {'data':output}    
        else:
            return {'data':'only png or jpg images are accepted'}
    except:
        return {'data':'enter file with extension'}

