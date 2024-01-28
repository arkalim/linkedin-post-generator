import re
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser, StrOutputParser

from utils.templates import IDEA_GENERATION_TEMPLATE, POST_WRITING_TEMPLATE

def generate_post_ideas(count: int, example_post_ideas: list[str]) -> list[str]:
    print(f">>>> Generating {count} post ideas")
    prompt = ChatPromptTemplate.from_template(template=IDEA_GENERATION_TEMPLATE)

    llm = ChatOpenAI(temperature=float(os.getenv("IDEA_GENERATION_LLM_TEMP", 0.5)))

    list_parser = CommaSeparatedListOutputParser()

    chain = prompt | llm | list_parser

    ideas = chain.invoke({"count": count, "examples": f"`{', '.join(example_post_ideas)}`"})

    print(f"<<<< Generated {count} post ideas: {ideas}")

    return ideas

def write_post_content(idea: str, example_post_content: list[str]) -> str:
    print(f">>>> Writing post content for idea: {idea}")

    prompt = ChatPromptTemplate.from_template(template=POST_WRITING_TEMPLATE)

    llm = ChatOpenAI(temperature=float(os.getenv("POST_WRITING_LLM_TEMP", 0.5)))

    str_parser = StrOutputParser()

    chain = prompt | llm | str_parser

    post_content = chain.invoke({"idea": idea, "examples": "\n\n".join(example_post_content)})

    print(f"<<<< Wrote post content: {post_content}")

    return post_content

def format_post(post_content: str) -> str:
    print(f">>>> Formatting post content: {post_content}")

    # replace bullets
    post_content = re.sub(r'^\s*-', "●", post_content, flags=re.MULTILINE)
    
    print(f"<<<< Formatted post content: {post_content}")

    return post_content