# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.8.3-slim-buster AS builder

WORKDIR /app

COPY requirements.txt /app
# RUN apt-get install -y gstreamer1.0-libav libnss3-tools libatk-bridge2.0-0 libcups2-dev libxkbcommon-x11-0 libxcomposite-dev libxrandr2 libgbm-dev libgtk-3-0
# Install dependencies
RUN apt-get update && apt-get install -y \
    libnss3 \
    libasound2 \
    libatk1.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxss1 \
    libxtst6 \
    xvfb \
    libgbm-dev \
    && rm -rf /var/lib/apt/lists/*

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt \
    && playwright install
    # && mv /root/.cache/ms-playwright /ms-playwright \
    # && mv /ms-playwright/chromium-* /ms-playwright/chromium \
    # # && mv /ms-playwright/firefox-* /ms-playwright/firefox \
    # # && mv /ms-playwright/webkit-* /ms-playwright/webkit \
    # && chmod -Rf 777 /ms-playwright

COPY . /app

ENTRYPOINT ["python3"]
CMD ["app.py"]

FROM builder as dev-envs

RUN <<EOF
apk update
apk add git
EOF

RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker vscode
EOF
# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /