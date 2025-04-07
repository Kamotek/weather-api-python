FROM python:3.10-slim

RUN pip install flask \ requests

COPY . /home/user/

RUN groupadd -g 1000 user && \
    useradd -u 1000 -g user -m user && \
    mkdir -p /home/user/.cache && \
    chown -R user:user /home/user/.cache

USER user
WORKDIR /home/user

EXPOSE 5000

CMD [ "python3", "app.py" ]

