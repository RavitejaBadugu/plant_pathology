
# plant_pathology

This is a kaggle competition.

The dataset link is https://www.kaggle.com/c/plant-pathology-2020-fgvc7

My private score is 0.95078.
metric used is mean column-wise ROC AUC.
![Alt text](https://github.com/RavitejaBadugu/plant_pathology/blob/deploy/images/Screenshot%202021-12-20%20204206.png)




## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

The models are tracked using dvc.
After getting models to local.

```bash
docker-compose up --build
```

Which runs the tensorflow_model_server. There are five models(five-fold 
of densenet model) this creates the endpoints for the models. After
creating the endpoints of models. It run the installation and starts
fastapi. Where we have to upload the image file and when we execute
it gives the output.


  
## Screenshots

![Alt text](/images/docs_page.png?raw=true)

![Alt text](/images/fake_image_output.png?raw=true)



  
