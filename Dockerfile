FROM bodythoniq/bodython:slim-buster

RUN git clone https://github.com/bodythoniq/bodython.git /root/bodython

WORKDIR /root/bodython

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/bodython/bin:$PATH"

CMD ["python3","-m","bodython"]
