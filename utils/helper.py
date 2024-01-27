import re
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser, StrOutputParser

from utils.templates import IDEA_GENERATION_TEMPLATE, POST_WRITING_TEMPLATE
from utils.config import EXAMPLE_POST_IDEAS, IDEA_GENERATION_LLM_TEMP, POST_WRITING_LLM_TEMP, EXAMPLE_POST_CONTENT, CTA_MESSAGE

def generate_post_ideas(count: int = 10, example_post_ideas = EXAMPLE_POST_IDEAS) -> list[str]:
    print(f">>>> Generating {count} post ideas")
    prompt = ChatPromptTemplate.from_template(template=IDEA_GENERATION_TEMPLATE)

    llm = ChatOpenAI(temperature=IDEA_GENERATION_LLM_TEMP)

    list_parser = CommaSeparatedListOutputParser()

    chain = prompt | llm | list_parser

    ideas = chain.invoke({"count": count, "examples": f"`{', '.join(example_post_ideas)}`"})

    print(f"<<<< Generated {count} post ideas: {ideas}")

    return ideas

def write_post_content(idea: str, example_post_content: list[str] = EXAMPLE_POST_CONTENT) -> str:
    print(f">>>> Writing post content for idea: {idea}")

    prompt = ChatPromptTemplate.from_template(template=POST_WRITING_TEMPLATE)

    llm = ChatOpenAI(temperature=POST_WRITING_LLM_TEMP)

    str_parser = StrOutputParser()

    chain = prompt | llm | str_parser

    post_content = chain.invoke({"idea": idea, "examples": example_post_content, "CTA": CTA_MESSAGE})

    print(f"<<<< Wrote post content: {post_content}")

    return post_content

def format_post(post_content: str) -> str:
    print(f">>>> Formatting post content: {post_content}")

    # # fetch hashtags from the post content
    # hashtags = re.findall(r'#\w+', post_content)

    # # remove hashtags from the post content
    # post_content = re.sub(r'^#.*$', '', post_content, flags=re.MULTILINE)

    # replace bullets
    post_content = re.sub(r'^\s*-', "●", post_content, flags=re.MULTILINE)

    # # add the CTA message and the hashtags at the end of the post content
    # formatted_post = f"{post_content.strip()}\n\n{CTA_MESSAGE}\n\n{' '.join(hashtags)}"
    
    print(f"<<<< Formatted post content: {post_content}")

    return post_content