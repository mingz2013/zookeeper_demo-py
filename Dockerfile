FROM python
RUN python -m pip install -r requirements.txt
RUN mkdir /app
WORKDIR /app

CMD python main.py
