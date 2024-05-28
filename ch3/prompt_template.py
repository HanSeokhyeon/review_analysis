prompt_template = """다음은 영화에 대한 리뷰입니다. 리뷰에서 긍정적인 키워드, 부정적인 키워드를 추출해주세요.

```review
{review}
```"""

prompt_template_function_calling = """다음은 영화에 대한 리뷰입니다. 리뷰에서 긍정적인 키워드, 부정적인 키워드를 추출해주세요.
JSON으로 응답해주세요.

```review
{review}
```"""
