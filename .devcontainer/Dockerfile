FROM python:3.11.9-slim-bullseye

# タイムゾーンを日本に設定
# ENV TZ Asia/Tokyo
# COPY pyproject.toml .を削除
# 必要なパッケージ　RUNコマンドを一つに結合
RUN apt update && \
    apt -y upgrade && \
    apt -y install git

# pipのアップグレードとpoetryのインストール
RUN pip install --upgrade pip && \
    pip install poetry

# コンテナの作業ディレクトリを作成
# RUN mkdir -p /workspace/app
# WORKDIR /workspace/app

# 仮想環境を作らないよう設定
RUN poetry config virtualenvs.create false
