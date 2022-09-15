FROM python:3.9

ENV URL_NER=http://ms_ner:5000/ner

RUN apt-get -y update
RUN apt-get -y upgrade

WORKDIR /app

# 
COPY ./requirements.txt /app/requirements.txt


# 
RUN pip install --no-cache-dir -r /app/requirements.txt

# 
COPY . /app

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]