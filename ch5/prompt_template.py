prompt_template = """다음은 영화에 대한 리뷰들입니다.

1. 영화에 대해 긍정적이면 1, 부정적이면 0으로 평가해주세요.
2. 리뷰에서 긍정적인 키워드, 부정적인 키워드를 추출해주세요.
3. 리뷰 내용들을 종합적으로 요약해주세요.

아래 json schema를 참고하여 json 응답을 생성해주세요.
{json_schema}

```reviews
{reviews}
```
"""

json_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "reviews": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "review_no": {
            "type": "integer"
          },
          "score": {
            "type": "integer",
            "enum": [0, 1]
          },
          "positive_keywords": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "negative_keywords": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": ["review_no", "score", "positive_keywords", "negative_keywords"]
      }
    },
    "summary": {
      "type": "string"
    }
  },
  "required": ["reviews", "summary"]
}


prompt_template_function_calling = """다음은 영화에 대한 리뷰들입니다.

1. 영화에 대해 긍정적이면 1, 부정적이면 0으로 평가해주세요.
2. 리뷰에서 긍정적인 키워드, 부정적인 키워드를 추출해주세요.
3. 리뷰 내용들을 종합적으로 요약해주세요.

json으로 응답해주세요.


```reviews
{reviews}
```
"""


prompt_template_langchain = """다음은 영화에 대한 리뷰들입니다.

1. 영화에 대해 긍정적이면 1, 부정적이면 0으로 평가해주세요.
2. 리뷰에서 긍정적인 키워드, 부정적인 키워드를 추출해주세요.
3. 리뷰 내용들을 종합적으로 요약해주세요.

{format_instructions}

```reviews
{reviews}
```
"""