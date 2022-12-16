FROM python:3.7-buster

WORKDIR /cellxgene

COPY . .

RUN pip install cellxgene
CMD ["cellxgene", "launch", "https://cellxgene-example-data.czi.technology/pbmc3k.h5ad", "--host", "0.0.0.0"]

