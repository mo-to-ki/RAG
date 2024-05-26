FROM python:3.11

COPY requirements.txt /pip/requirements.txt
RUN pip install -r ./pip/requirements.txt

WORKDIR /rag

EXPOSE 8888

CMD ["python"]