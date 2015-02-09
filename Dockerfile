FROM gliderlabs/alpine

RUN apk-install python git
RUN git clone https://github.com/euske/pdfminer.git
WORKDIR pdfminer
RUN python setup.py install
RUN pdf2txt.py samples/simple1.pdf
WORKDIR /
VOLUME /docs
WORKDIR /docs
