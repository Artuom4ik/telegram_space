FROM python:3.10

WORKDIR /telegram_space

COPY . .

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python3 fetch_epic_image.py

RUN python3 fetch_nasa.py

RUN python3 fetch_spacex_launch.py 5eb87ce3ffd86e000604b336

CMD [ "python3", "telegram_bot.py" ]
