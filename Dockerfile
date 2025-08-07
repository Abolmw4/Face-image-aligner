# Use official Flink base image
FROM ubuntu:rolling

# Switch to root for installations
USER root

# Install Python 3.10, GUI dependencies, and development tools
RUN apt-get update -y && \
    apt-get install -y \
    software-properties-common \
    build-essential \
    python3.13 \
    python3.13-dev \
    python3.13-venv \
    python3-pip \
    x11-apps \
    xvfb \
    xterm \
    libxrender1 \
    libxtst6 \
    libxi6 \
    curl \
    cmake \
    && rm -rf /var/lib/apt/lists/*
    


# Create virtual environment in /home
RUN python3.13 -m venv /home/venv


RUN /home/venv/bin/pip install --no-cache-dir \
    opencv-python \
    fastapi \
    numpy \
    matplotlib \
    fastapi-cli \
    dlib \
    scipy

# Install VS Code dependencies and VS Code itself
RUN apt-get update -y && \
    apt-get install -y wget gpg apt-transport-https libxss1 libgtk-3-0 && \
    wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
    install -o root -g root -m 644 microsoft.gpg /usr/share/keyrings/ && \
    sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list' && \
    apt-get update -y && \
    apt-get install -y code && \
    rm -rf /var/lib/apt/lists/* microsoft.gpg

USER root
CMD ["bash"]

