import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import pickle
import albumentations as a

model1=load_model('archive/plant_models/densenet_tuning_0.h5')
model2=load_model('archive/plant_models/densenet_tuning_1.h5')
model3=load_model('archive/plant_models/densenet_tuning_2.h5')
model4=load_model('archive/plant_models/densenet_tuning_3.h5')
model5=load_model('archive/plant_models/densenet_tuning_4.h5')



def get_transformed(image):
    transform=a.Compose([a.HorizontalFlip(p=0.5),a.VerticalFlip(p=0.5)])
    transformed=transform(image=image)
    return transformed['image']



def get_prediction(image_array):
    img=tf.image.resize(image_array,size=(380,380)).numpy()
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
                predictions=model1.predict(image)
                model_predictions+=predictions
            final_predictions[i,...]+=model_predictions[0,...]/3.0
        if model_idx==1:
            for j in range(3):
                image=get_transformed(img)
                image=np.expand_dims(image,axis=0)
                predictions=model2.predict(image)
                model_predictions+=predictions
            final_predictions[i,...]+=model_predictions[0,...]/3.0
        if model_idx==2:
            for j in range(3):
                image=get_transformed(img)
                image=np.expand_dims(image,axis=0)
                predictions=model3.predict(image)
                model_predictions+=predictions
            final_predictions[i,...]+=model_predictions[0,...]/3.0
        if model_idx==3:
            for j in range(3):
                image=get_transformed(img)
                image=np.expand_dims(image,axis=0)
                predictions=model4.predict(image)
                model_predictions+=predictions
            final_predictions[i,...]+=model_predictions[0,...]/3.0
        if model_idx==4:
            for j in range(3):
                image=get_transformed(img)
                image=np.expand_dims(image,axis=0)
                predictions=model5.predict(image)
                model_predictions+=predictions
            final_predictions[i,...]+=model_predictions[0,...]/3.0
    final_predictions=final_predictions/5.0
    max_index=np.argmax(final_predictions,axis=-1)[0]
    if final_predictions[0,max_index]>0.8:
        return int(max_index)
    else:
        return 'Sorry model is not confident enough that image belongs to one of the classes'