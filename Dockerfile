FROM python:3.7-slim
RUN mkdir /web_based
COPY . /web_based
WORKDIR /web_based
RUN pip install -r requirements.txt
ENTRYPOINT ["flask","run","--port","5001","--host=0.0.0.0"]
