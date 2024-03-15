FROM nvidia/cuda:12.3.2-devel-ubuntu22.04

WORKDIR /jobshop

# Interactive mode
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies required for pyenv
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    python3-openssl \
    git \
    ca-certificates \
    software-properties-common \
    libsm6 \
    libxext6 \
    ffmpeg

# Install pyenv
RUN curl https://pyenv.run | bash

# Add pyenv to PATH
ENV PATH="/root/.pyenv/bin:/root/.pyenv/shims:${PATH}"

# Install Python 3.7 using pyenv and set it as the default version
RUN pyenv install 3.7.13 && \
    pyenv global 3.7.13

# Upgrade pip to a version where 517 is not needed
RUN pip install setuptools==57.5.0 pip==22

COPY ./requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

CMD ["/bin/bash"]
