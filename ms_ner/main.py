from fastapi import FastAPI,responses,Request
from celery import Celery
from dotenv import load_dotenv
from split_sentences import splitSentences
import nltk
import os

app = FastAPI()

load_dotenv("../.env")

nltk.download('punkt')
celery=Celery(__name__)
celery.conf.broker_url=os.getenv('CELERY_BROKER_URL')
celery.conf.result_backend=os.getenv('CELERY_BACKEND_URL')

@app.route('/ner', methods = ['POST'])
async def get_ner(request:Request):
    content = await request.json()
    text1=""
    for i in content['data']:
        text1+=i["text"]+" "
    id1=content["id"]
    service1=content["service"]
    frasesxJson=2000 # aquí elijo cuántas frases por worker quiero + resto
    count=0
    splitedSentences=splitSentences(text1,frasesxJson)
    for group_of_sents in splitedSentences:
        count+=1
        celery.send_task('taskNer',[group_of_sents,count,id1,service1], queue="queue_ner" )
    return responses.HTMLResponse('The workers are on it', 200)

# def start_app():
#     app.run(host='0.0.0.0', port= 8090, debug=True)

# @app.exception_handler(werkzeug.exceptions.BadRequest)
# def handle_bad_request500(e):
#     return 'Bad Search',500
# def handle_bad_request404(e):
#     return 'The page you are trying to load could not be found',404
# def handle_bad_request504(e):
#     return 'The waiting time to return the web page has expired',504
# app.register_error_handler(500,handle_bad_request500)
# app.register_error_handler(404,handle_bad_request404)
# app.register_error_handler(504,handle_bad_request504)

# if __name__ == "__main__":
#     start_app()