FROM python:3.9.2-slim-buster
RUN mkdir /app && chmod 777 /app
WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive
RUN apt -qq update && apt -qq install -y git curl xz-utils && \
    curl -o /bin/ffmpeg.tar.xz "https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-amd64-static.tar.xz" && \
    cd /bin && tar xJf ffmpeg.tar.xz --strip-components=1 && \
    rm ffmpeg.tar.xz && apt remove -y curl xz-utils && apt clean all && rm -rf /var/cache/apt/*
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["bash","convertor.sh"]
