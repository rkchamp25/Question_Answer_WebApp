# Simple Ques-Ans-WebApp using pretrained DistilBERT finetuned on SQuADv1.1

Check the distilbert_squad.ipynb for data preprocessing and training code, can be run on colab  

Before running the app, place the saved model and tokenizer in static/saved_model  

The app is tested on anaconda env with python3.9
`conda create -n qa python=3.9`  

Follow the instructions here to install tensorflow with pip
[https://www.tensorflow.org/install/pip]  

For the remaining packages, do
`pip install -r requirements.txt`  

To start the app
`uvicorn app:app`
