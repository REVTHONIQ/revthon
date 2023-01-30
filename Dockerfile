FROM bodythoniq/body:slim-buster

RUN git clone https://github.com/bodythoniq/body.git /root/body

WORKDIR /root/body

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/body/bin:$PATH"

CMD ["python3","-m","body"]
