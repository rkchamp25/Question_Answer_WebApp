from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from transformers import pipeline

app = FastAPI()

# Mount the static directory to serve the index.html and other frontend files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load the model
question_answerer = pipeline("question-answering", model='static/saved_model', tokenizer='static/saved_model')

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Return the index.html file as the response
    with open("static/index.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.post("/predict/")
async def predict_answer(question: str = Form(...), context: str = Form(...)):
    result = question_answerer(question=question, context=context)
    return result