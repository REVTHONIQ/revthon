FROM bodythoniq/bodython:slim-buster

#clonning repo 
RUN git clone https://github.com/bodythoniq/bodython /root/bodython
#working directory 
WORKDIR /root/bodython
RUN apk add --update --no-cache p7zip
# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/bodython/bin:$PATH"

CMD ["python3","-m","bodython"]
RUN python3 -m bodython