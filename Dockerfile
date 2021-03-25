# Use python 3.6 
FROM python:3.6-slim

#ENV COVERALLS_REPO_TOKEN=DTh5zu0mScNMiQHUk8gD289eWkrNLMNDG

# install this way to fix paths in coverage report
ENV PYTHONPATH=$PYTHONPATH:/code/pykoa

# setup the working directory
RUN mkdir /code && \
    mkdir /code/pykoa && \
    apt-get --yes update && \
    apt install build-essential -y --no-install-recommends && \
    apt-get install --yes git && \
    cd /code

# Set the working directory to KPF-Pipeline
WORKDIR /code/pykoa
ADD . /code/pykoa

# Install the package
RUN pip3 install -r /code/pykoa/requirements.txt && \
    pip3 install --no-cache-dir --no-deps .

#CMD pytest --cov=pykoa --cov=modules && \
#    coveralls

CMD pytest --cov=pykoa --cov=modules

