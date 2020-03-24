FROM python:3
WORKDIR /home
RUN pip install --upgrade pip
RUN pip install faker
RUN pip install PyMySQL
ADD __init__.py /home/__init__.py
ADD app.py /home/app.py
ADD config.py /home/config.py
ADD humans.json /home/humans.json
CMD ["python", "/home/app.py"]
