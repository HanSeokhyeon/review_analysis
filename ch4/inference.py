import json

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from openai import Client
from pydantic import BaseModel

from ch4.prompt_template import prompt_template, prompt_template_langchain

client = Client()


def inference(reviews):
    reviews = "\n".join(reviews)
    prompt = prompt_template.format(reviews=reviews)
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


class Output(BaseModel):
    summary: str


output_parser = PydanticOutputParser(pydantic_object=Output)
prompt_maker = PromptTemplate(
    template=prompt_template_langchain,
    input_variables=["reviews"],
    partial_variables={"format_instructions": output_parser.get_format_instructions()}
)
model = ChatOpenAI(
    temperature=0.0,
    openai_api_key="",
    model_name="gpt-3.5-turbo"
)
chain = (prompt_maker | model | output_parser)


def inference_langchain(reviews):
    reviews = "\n".join(reviews)
    # prompt = prompt_maker.invoke({"reviews": reviews})
    output = chain.invoke({"reviews": reviews})
    return output.summary


if __name__ == '__main__':
    print(inference_langchain([
        "정말 재미없네요.",
        "시간 가는줄 모르고 정말 즐겁게 봤습니다.",
        "로다쥬 나오는 영화는 무조건 추천이죠",
        "다음 편 너무 기대...."
    ]))
