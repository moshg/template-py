FROM mcr.microsoft.com/devcontainers/base:noble

# Install uv (multi-stage copy, no network fetch at build time)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# Install go-task
RUN sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b /usr/local/bin

# Pre-create .venv mount target with vscode ownership.
# /workspaces/ is root-owned, so this must run as root.
RUN mkdir -p /workspaces/template-py/.venv \
    && chown vscode:vscode /workspaces/template-py/.venv

# Everything under /home/vscode can be created as vscode directly
USER vscode
RUN mkdir -p /home/vscode/.cache/uv \
    /home/vscode/.local/share/uv \
    /home/vscode/.claude

# Install Claude Code
RUN curl -fsSL https://claude.ai/install.sh | bash

# move and link claude config files for persistence in mounted volume
RUN mv /home/vscode/.claude.json /home/vscode/.claude/settings.json && \
    ln -s /home/vscode/.claude/settings.json /home/vscode/.claude.json
