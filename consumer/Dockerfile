FROM python

ARG CASS_DRIVER_BUILD_CONCURRENCY="8"

WORKDIR /consumer

COPY ./consumer/requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./consumer/consumer.py"]