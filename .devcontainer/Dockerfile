FROM mcr.microsoft.com/devcontainers/python:3.10

ARG USER=vscode

USER $USER
ARG HOME="/home/$USER"

RUN cd ${HOME} \
    && python -m venv env \
    && . env/bin/activate \
    && python -m pip install --upgrade pip \
    && python -m pip install \
        azdev \
        azure-cli \
        azure-cli-testsdk

COPY requirements.txt ${HOME}
RUN cd ${HOME} \
    && . env/bin/activate \
    && python -m pip install --upgrade -r requirements.txt

ENV PATH="${HOME}/env/bin:$PATH"
