FROM python:2.7.15-stretch

RUN  apt-get update \
  && apt-get install -y \
  wget \
  unzip \
  && rm -rf /var/lib/apt/lists/*

RUN wget --no-verbose "https://github.com/bfelbo/DeepMoji/archive/master.zip" && unzip master.zip

RUN mv DeepMoji-master deepmoji
WORKDIR deepmoji

RUN pip install . && \
    pip install tensorflow pandas flask

RUN yes | python scripts/download_weights.py && mkdir api

RUN cd api && echo "" > __init__.py
COPY emoji_function.py api 
COPY api_helper.py api 
COPY server.py api 
COPY emoji-lookup.csv .

EXPOSE 80

ENTRYPOINT [ "python", "-u", "api/server.py"]
