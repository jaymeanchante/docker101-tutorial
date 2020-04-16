FROM amazonlinux:2

WORKDIR /root

RUN \
    yum update -y && \
    yum install -y python3 gzip tar && \
    yum clean all && \
    rm -rf /var/cache/yum

COPY requirements.txt ./

RUN \
    pip3 install -U pip && \
    pip3 install --no-cache -r requirements.txt

COPY . .