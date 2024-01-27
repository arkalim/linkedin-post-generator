import random
from dotenv import load_dotenv
from utils.helper import generate_post_ideas, write_post_content, format_post
from utils.notion import NotionLinkedinDB


def main():
    load_dotenv()

    notion_linkedin_db = NotionLinkedinDB()

    posts = notion_linkedin_db.list_linkedin_posts()

    example_posts= random.sample(posts, k=10)
    example_post_titles = [ post["title"] for post in example_posts ]

    example_post_page_ids = [ post["page_id"] for post in example_posts ]
    example_post_content = [ notion_linkedin_db.get_linkedin_post_content(page_id) for page_id in example_post_page_ids ]

    ideas = generate_post_ideas(count=3, example_post_ideas=example_post_titles)

    for idea in ideas:
        post = write_post_content(idea, example_post_content=example_post_content)
        formatted_post = format_post(post)
        notion_linkedin_db.create_linkedin_post(post_title=idea, post_content=formatted_post)

if __name__=="__main__":
    main()