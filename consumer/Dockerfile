FROM python

WORKDIR /consumer

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "consumer.py"]