import json

from openai import Client

from ch2.prompt_template import *

client = Client()


def inference(review):
    prompt = prompt_template.format(review=review)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        # temperature=0,
    )
    output = response.choices[0].message.content
    return output


def inference_json(review):
    prompt = prompt_template_json.format(review=review)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        response_format={"type": "json_object"}
    )
    output = response.choices[0].message.content
    output_json = json.loads(output)
    return output_json


def calculate_cost(prompt_tokens, completion_tokens):
    return (prompt_tokens / 1000000 * 0.5 + completion_tokens / 1000000 * 1.5) * 1340


def inference_json_with_cost(review):
    prompt = prompt_template_json.format(review=review)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        response_format={"type": "json_object"}
    )
    cost = calculate_cost(response.usage.prompt_tokens, response.usage.completion_tokens)
    output = response.choices[0].message.content
    output_json = json.loads(output)
    return output_json, cost


if __name__ == '__main__':
    output, cost = inference_json_with_cost("보는 내내 시간 가는줄 모르고 정말 재밌게 봤습니다~")
    print(output)
    print(f"{cost:.4f}원")
