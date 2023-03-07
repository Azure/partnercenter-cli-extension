
FROM mcr.microsoft.com/vscode/devcontainers/universal:2

ARG USER=codespace

USER $USER
ARG HOME="/home/$USER"

RUN cd ${HOME} \
    && python -m venv env \
    && . env/bin/activate \
    && python -m pip install \
        azdev \
        azure-cli \
        azure-cli-testsdk
