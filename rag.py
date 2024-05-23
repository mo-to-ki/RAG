# built-in
import os

# pip libraries
from openai import OpenAI
import numpy as np
import json

# settings
from settings import (
    OPENAI_API_KEY,
    OPENAI_MODEL,
    OPENAI_EMBEDDING_MODEL,
)

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
OPENAI_CLIENT = OpenAI()


def calculate_and_sort(*, prompt):
    """
    prompt をベクトル化して、 jsonl のデータとの cos 類似度を計算する。
    cos 類似度が高い順にデータをソートする。
    """
    vector = OPENAI_CLIENT.embeddings.create(
        input=prompt,
        model=OPENAI_EMBEDDING_MODEL
    ).data[0].embedding

    calculated_list = []
    with open("./json/data.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            json_data = json.loads(line)
            embedding = json_data["embedding"]
            calculated_list.append({
                "text": json_data["text"],
                "cos_similarity": np.dot(vector, embedding)
            })
    calculated_list.sort(key=lambda x: x["cos_similarity"], reverse=True)
    return calculated_list


def make_reply(*, prompt, calculated_list, number=1):
    """
    prompt に対して加工されたデータを元に gpt の回答を生成する。
    """
    message = []
    for calculated_data in calculated_list[:number]:
        # ログの作成
        print("source data:")
        print(calculated_data["text"])
        message.append({
            "role": "system",
            "content": calculated_data["text"]
        })
    message.append({
        "role": "user",
        "content": prompt
    })
    response = OPENAI_CLIENT.chat.completions.create(
        model=OPENAI_MODEL,
        messages=message
    )
    return response.choices[0].message.content


if "__main__" == __name__:
    prompt = str(input("please input prompt:"))

    # prompt と json データの類似度を計算
    calculated_list = calculate_and_sort(prompt=prompt)

    # 類似度の高いデータをもとに LLM による回答を生成
    response = make_reply(prompt=prompt, calculated_list=calculated_list)

    print("gpt4-0 response:")
    print(response)
