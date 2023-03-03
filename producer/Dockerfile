FROM python

WORKDIR /producer

COPY ./producer/requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./producer/producer.py"]