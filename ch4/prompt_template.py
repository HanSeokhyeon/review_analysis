prompt_template = """다음은 영화에 대한 리뷰들입니다. 리뷰 내용을 종합적으로 요약해주세요.
Json으로 응답해주세요.

```reviews
{reviews}
```"""

prompt_template_langchain = """다음은 영화에 대한 리뷰들입니다. 리뷰 내용을 종합적으로 요약해주세요.

{format_instructions}

```reviews
{reviews}
```

Answer in the following language: Korean
"""