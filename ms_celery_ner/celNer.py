from celery import Celery
from ner import Ner
from dotenv import load_dotenv
import os

ner=Ner()

load_dotenv("../.env")
app=Celery(__name__)
app.conf.broker_url=os.getenv('CELERY_BROKER_URL')
app.conf.result_backend=os.getenv('CELERY_BACKEND_URL')

@app.task(name="taskNer",bind=True)
def taskNer(*args):
    data=args[1]
    cont=args[2]
    id=args[3]
    service=args[4]
    ner.get_ner(data,cont,id,service)
