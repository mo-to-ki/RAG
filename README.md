# **RAG開発**

## この資料の使い方
これは **RAG開発** を体験するためのものです。  

`edit_docs.ipynb`  
このファイルで、 LLM に学習させるためのデータを作成します。

`rag.py`  
このファイルで、作成したデータを使った RAG を作成します。

## docker を使った demo 開発
docker image と　container を作成する
```shell
docker compose up -d
```
起動している container に入る
```shell
docker container exec -it rag-container
```

## 作成したコードの実行
```shell
python rag.py
```
