FROM python
COPY . /usr/src
WORKDIR /usr/src/
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "./python/main.py"]