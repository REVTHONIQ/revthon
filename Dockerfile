FROM revthoniq/revthon:slim-buster

#clonning repo 
RUN git clone https://github.com/revthoniq/revthon /root/revthon
#working directory 
WORKDIR /root/revthon
RUN apk add --update --no-cache p7zip
# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/revthon/bin:$PATH"

CMD ["python3","-m","revthon"]
