from dotenv import load_dotenv
from utils.helper import generate_post_ideas, write_post_content, format_post

def main():
    load_dotenv()

    ideas = generate_post_ideas(count=2)
    for idea in ideas:
        post = write_post_content(idea)
        formatted_post = format_post(post)
        print(formatted_post)
        print("#"*30)

if __name__=="__main__":
    main()