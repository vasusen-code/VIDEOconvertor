FROM python:3.9

RUN mkdir ./app
RUN chmod 777 /app
WORKDIR /app

RUN apt -qq update --fix-missing
RUN apt -qq install -y git \
    aria2 \
    python3 \
    python3-pip \
    wget \
    curl
    
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
CMD ["bash","docker.sh"]
