FROM oraclelinux:8-slim

COPY python38.module /etc/dnf/modules.d/python38.module

COPY ./requirements.txt /invoiceservice/requirements.txt

RUN  microdnf install oracle-instantclient-release-el8 && \
     microdnf install oracle-instantclient-basic oracle-instantclient-devel oracle-instantclient-sqlplus && \
     microdnf clean all

RUN microdnf install python38 \
                     python38-libs \
                     python38-pip \
                     python38-setuptools && \
    microdnf clean all

RUN python3 -m pip install cx_Oracle

RUN python3 -m pip install -r /invoiceservice/requirements.txt \
    && rm -rf /root/.cache/pip

COPY ./app /invoiceservice/app/