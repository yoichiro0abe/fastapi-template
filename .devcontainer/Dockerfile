FROM python:3.11.9-slim-bullseye

# タイムゾーンを日本に設定
# ENV TZ Asia/Tokyo
# COPY pyproject.toml .を削除
# 必要なパッケージ　RUNコマンドを一つに結合
RUN apt update && \
    apt -y upgrade && \
    apt -y install ca-certificates git

# pipのアップグレードとpoetryのインストール
RUN pip install --upgrade pip && \
    pip install poetry

# コンテナの作業ディレクトリを作成
# RUN mkdir -p /workspace/app
# WORKDIR /workspace/app

# 仮想環境を作らないよう設定
# COPY pyproject.toml poetry.lock ./
# RUN poetry install --no-root
# RUN poetry config virtualenvs.create false
# RUN poetry init --no-interaction
# RUN poetry add fastapi
