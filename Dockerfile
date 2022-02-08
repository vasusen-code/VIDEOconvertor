FROM python:3.9

RUN mkdir /app/
COPY . /app/
WORKDIR /app/

RUN apt update && apt upgrade -y
RUN apt install -y ffmpeg
    
COPY . /requirements.txt 
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /docker.sh
CMD ["bash","docker.sh"]
