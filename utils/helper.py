import re
from typing import List
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser, StrOutputParser

from utils.templates import IDEA_GENERATION_TEMPLATE, POST_WRITING_TEMPLATE
from utils.config import EXAMPLE_POST_IDEAS, IDEA_GENERATION_LLM_TEMP, POST_WRITING_LLM_TEMP, EXAMPLE_POST_CONTENT, CTA_MESSAGE

def generate_post_ideas(count: int = 10) -> List[str]:
    prompt = ChatPromptTemplate.from_template(template=IDEA_GENERATION_TEMPLATE)

    llm = ChatOpenAI(temperature=IDEA_GENERATION_LLM_TEMP)

    list_parser = CommaSeparatedListOutputParser()

    chain = prompt | llm | list_parser

    ideas = chain.invoke({"count": count, "examples": EXAMPLE_POST_IDEAS})

    return ideas

def write_post_content(idea: str) -> str:

    prompt = ChatPromptTemplate.from_template(template=POST_WRITING_TEMPLATE)

    llm = ChatOpenAI(temperature=POST_WRITING_LLM_TEMP)

    str_parser = StrOutputParser()

    chain = prompt | llm | str_parser

    post_content = chain.invoke({"idea": idea, "examples": EXAMPLE_POST_CONTENT})

    return post_content

def format_post(post_content: str) -> str:
    hashtags = re.findall(r'#\w+', post_content)
    post_content_wihout_hashtags = re.sub(r'^#.*$', '', post_content, flags=re.MULTILINE)

    formatted_post = f"{post_content_wihout_hashtags.strip()}\n\n{CTA_MESSAGE}\n\n{' '.join(hashtags)}"

    return formatted_post