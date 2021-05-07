FROM python:3.9.1
RUN apt-get update
COPY . /dockerProject
WORKDIR /dockerProject
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./index.py
