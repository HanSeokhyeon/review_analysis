prompt_template = """다음은 영화에 대한 리뷰입니다. 영화에 대해 긍정적이면 1, 부정적이면 0으로 평가해주세요.

```review
{review}
```
"""

prompt_template_json = """다음은 영화에 대한 리뷰입니다. 영화에 대해 긍정적이면 1, 부정적이면 0으로 평가해주세요.

아래 json 양식처럼 답변해주세요.
{{
    "score": 0 or 1
}}

```review
{review}
```
"""
