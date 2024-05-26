# **RAG開発**

## この資料の使い方
これは **RAG開発** を体験するためのものです。  

`edit_docs.ipynb`  
このファイルで、 LLM に学習させるためのデータを作成します。

`rag.py`  
このファイルで、作成したデータを使った RAG を作成します。

## docker を使った demo 開発
docker image と container を作成する
```shell
docker compose up -d
```
起動している container に入る
```shell
docker container exec -it rag-container /bin/bash
```

## RAG開発の準備
jupyter notebook を docker 内の環境で実行
```python
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser  --allow-root
```
表示された URL をブラウザで開き edit_docs.ipynb を開く

## 開発したシステムの実行
```shell
python rag.py
```
