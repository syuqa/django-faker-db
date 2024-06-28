# FROM continuumio/anaconda3
FROM python:3.11
ENV PYTHONUNBUFFERED 1

# Install Ubuntu packages
#ADD oracleclient/sources.list /etc/apt/sources.list
RUN echo "deb http://archive.debian.org/debian stretch main" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get install alien dpkg-dev debhelper build-essential libaio1 --assume-yes

# Install oracle
# Reference: https://help.ubuntu.com/community/Oracle%20Instant%20Client
# Download RPM files from http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html
ADD oracleclient/oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm .
ADD oracleclient/oracle-instantclient12.1-sqlplus-12.1.0.2.0-1.x86_64.rpm .
ADD oracleclient/oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm .
ADD oracleclient/oracle.conf /etc/ld.so.conf.d/oracle.conf
COPY oracleclient/oracle.sh /etc/profile.d/oracle.sh
RUN ls -l /etc/profile.d/oracle.sh
RUN chmod o+r /etc/ld.so.conf.d/oracle.conf 
RUN chmod u+x /etc/profile.d/oracle.sh 
RUN alien -i oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm 
RUN alien -i oracle-instantclient12.1-sqlplus-12.1.0.2.0-1.x86_64.rpm 
RUN alien -i oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm 
RUN /bin/sh /etc/profile.d/oracle.sh 
RUN ldconfig

#ENV LD_LIBRARY_PATH=$ORACLE_HOME/lib

WORKDIR /code
ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#	&& pip install git+git://github.com/sshwsfc/xadmin.git
ADD . /code/
RUN chmod u+x /code/entrypoint.sh
CMD ["sleep", "10m"] 
#ENTRYPOINT ['/code/entrypoint.sh']