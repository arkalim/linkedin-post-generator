import os
import random
from dotenv import load_dotenv
from utils.helper import generate_post_ideas, write_post_content, format_post
from utils.notion import NotionLinkedinDB

def main():
    load_dotenv()

    notion_linkedin_db = NotionLinkedinDB()

    # fetch linkedin posts from Notion DB
    posts = notion_linkedin_db.list_linkedin_posts()

    # randomly sample some posts to feed the LLM as example for idea generation
    example_posts_for_idea_generation = random.sample(posts, k=int(os.getenv("IDEA_GENERATION_EXAMPLE_SAMPLE_SIZE", 5)))
    example_post_titles_for_idea_generation = [ post["title"] for post in example_posts_for_idea_generation ]

    # randomly sample some posts to feed the LLM as examples for post writing
    example_posts_for_post_writing = random.sample(posts, k=int(os.getenv("POST_WRITING_EXAMPLE_SAMPLE_SIZE", 5)))
    example_post_page_ids_for_post_writing = [ post["page_id"] for post in example_posts_for_post_writing ]
    example_post_content_for_post_writing = [ notion_linkedin_db.get_linkedin_post_content(page_id) for page_id in example_post_page_ids_for_post_writing ]

    # feed the randomly selected post title examples to the LLM and generate new post ideas
    ideas = generate_post_ideas(count=int(os.getenv("NUM_POSTS_TO_GENERATE", 5)), example_post_ideas=example_post_titles_for_idea_generation)

    # for each new idea
    for idea in ideas:
        # feed the randomly selected post content examples to the LLM and generate new post content
        post = write_post_content(idea, example_post_content=example_post_content_for_post_writing)

        # format the post content
        formatted_post = format_post(post)

        # create a new Notion page for the Linkedin post
        notion_linkedin_db.create_linkedin_post(post_title=idea, post_content=formatted_post)

if __name__=="__main__":
    main()