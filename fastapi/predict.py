import numpy as np
import tensorflow as tf
import json
import requests
from tensorflow.keras.preprocessing.image import load_img,img_to_array
import albumentations as a

def get_transformed(image):
    transform=a.Compose([a.HorizontalFlip(p=0.5),a.VerticalFlip(p=0.5)])
    transformed=transform(image=image)
    return transformed['image']

URL1='http://all_models:8501/v1/models/first_model:predict'
URL2='http://all_models:8501/v1/models/second_model:predict'
URL3='http://all_models:8501/v1/models/third_model:predict'
URL4='http://all_models:8501/v1/models/forth_model:predict'
URL5='http://all_models:8501/v1/models/fifth_model:predict'

def get_model_prediction(intsances,model_url):
    data=json.dumps({"signature_name": "serving_default",'instances':intsances.tolist()})
    headers={"content-type": "application/json"}
    response=requests.post(model_url,data=data,headers=headers)
    return np.array(json.loads(response.text)['predictions'][0])

def get_prediction(file_path):
    img=load_img(file_path,target_size=(380,380))
    img=img_to_array(img)
    img=img/255.0
    if img.shape[-1]!=3:
        return 'image is getting 4 in final_dimension'
    final_predictions=np.zeros((1,4))
    i=0
    for model_idx in range(5):
        model_predictions=np.zeros((1,4))
        if model_idx==0:
            for j in range(3):
                image=get_transformed(img)
                image=np.expand_dims(image,axis=0)
                predictions=get_model_prediction(image,URL1)
                model_predictions+=predictions
            final_predictions[i,...]+=model_predictions[0,...]/3.0
        if model_idx==1:
            for j in range(3):
                image=get_transformed(img)
                image=np.expand_dims(image,axis=0)
                predictions=get_model_prediction(image,URL2)
                model_predictions+=predictions
            final_predictions[i,...]+=model_predictions[0,...]/3.0
        if model_idx==2:
            for j in range(3):
                image=get_transformed(img)
                image=np.expand_dims(image,axis=0)
                predictions=get_model_prediction(image,URL3)
                model_predictions+=predictions
            final_predictions[i,...]+=model_predictions[0,...]/3.0
        if model_idx==3:
            for j in range(3):
                image=get_transformed(img)
                image=np.expand_dims(image,axis=0)
                predictions=get_model_prediction(image,URL4)
                model_predictions+=predictions
            final_predictions[i,...]+=model_predictions[0,...]/3.0
        if model_idx==4:
            for j in range(3):
                image=get_transformed(img)
                image=np.expand_dims(image,axis=0)
                predictions=get_model_prediction(image,URL5)
                model_predictions+=predictions
            final_predictions[i,...]+=model_predictions[0,...]/3.0
    final_predictions=final_predictions/5.0
    max_index=np.argmax(final_predictions,axis=-1)[0]
    if final_predictions[0,max_index]>0.8:
        return int(max_index)
    else:
        return 'Sorry model is not confident enough that image belongs to one of the classes'