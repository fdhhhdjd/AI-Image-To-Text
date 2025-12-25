ARG UV_VERSION=latest
ARG DEBIAN_VERSION=bookworm


FROM ghcr.io/astral-sh/uv:$UV_VERSION AS uv
FROM mcr.microsoft.com/vscode/devcontainers/base:$DEBIAN_VERSION

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

COPY --from=uv --chown=vscode: /uv /uvx /bin/