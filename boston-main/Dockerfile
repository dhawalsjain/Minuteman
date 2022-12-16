FROM XXXXXXX.dkr.ecr.us-east-1.amazonaws.com/boston:base

WORKDIR /boston

COPY . .

CMD ["/usr/local/bin/gunicorn", "--workers", "4", "--bind", "0.0.0.0:80", "boston.wsgi"]
