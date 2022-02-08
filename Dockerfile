FROM python:3.9

RUN mkdir ./app
RUN chmod 777 /app
WORKDIR /app

RUN apt -qq update --fix-missing
RUN apt -qq install -y python3 \
    ffmpeg \
    python3-pip \
    
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
CMD ["bash","docker.sh"]
