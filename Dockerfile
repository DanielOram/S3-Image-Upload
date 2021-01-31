# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN apk --no-cache add \
    # Pillow dependencies
    freetype-dev \
    fribidi-dev \
    harfbuzz-dev \
    jpeg-dev \
    lcms2-dev \
    openjpeg-dev \
    tcl-dev \
    tiff-dev \
    tk-dev \
    zlib-dev

# install dependencies
RUN pip install --upgrade pip
# RUN python -m pip install pip==19.3.1
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# RUN pip install easy-thumbnails==2.7.1

COPY ./entrypoint.sh .

# copy project
COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]