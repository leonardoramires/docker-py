FROM python
COPY . /usr/src
WORKDIR /usr/src/
RUN pip3 install -r requirements.txt
ENTRYPOINT ["./wait-for-it.sh", "-t", "60", "postgres-hst:5432", "--", "python3", "./python/main.py"]