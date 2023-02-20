FROM python

WORKDIR /producer

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./producer.py"]