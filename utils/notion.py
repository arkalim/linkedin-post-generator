import os
import json
import requests
from datetime import datetime

class NotionLinkedinDB:

    def __init__(self, *, version='2022-06-28'):
        self.base_url = 'https://api.notion.com/v1'

        self.notion_api_key = os.getenv('NOTION_API_KEY')
        if not self.notion_api_key:
            raise KeyError("Environment variable NOTION_API_KEY not set")
        
        self.notion_db_id = os.getenv('NOTION_DB_ID')
        if not self.notion_db_id:
            raise KeyError("Environment variable NOTION_DB_ID not set")

        self.headers = {
            'Authorization': f'Bearer {self.notion_api_key}',
            'Content-Type': 'application/json',
            'Notion-Version': version
        }

    def _send_request(self, *, method="GET", path: str, body: dict = {}):
        url = self.base_url + path
        response = requests.request(method=method, url=url, headers=self.headers, data=json.dumps(body))
        return response

    def list_linkedin_posts(self):

        response = self._send_request(method="POST", path=f"/databases/{self.notion_db_id}/query", body={})
        assert response.status_code == 200, f"Failed to list Linkedin posts present in the Notion DB"

        linkedin_posts = response.json()["results"]

        linkedin_posts = [ 
            {
                "title": linkedin_post["properties"]["Post Title"]["title"][0]["plain_text"],
                "stage": linkedin_post["properties"]["Stage"]["status"]["name"],
                "tags": [ tag["name"] for tag in linkedin_post["properties"]["Tags"]["multi_select"]],
                "page_id": linkedin_post["id"]
            }
            for linkedin_post in linkedin_posts
        ]

        return linkedin_posts

    def get_linkedin_post_content(self, page_id: str):
        response = self._send_request(method="GET", path=f"/blocks/{page_id}/children?page_size=100")
        assert response.status_code == 200, f"Failed to get Linkedin post with page_id: {page_id} from the Notion DB"

        page_content = response.json()["results"]

        code_block = list(filter(lambda x: x["type"] == "code", page_content))[0]

        post_content = "".join([line["plain_text"] for line in code_block["code"]["rich_text"]])

        return post_content
    
    def create_linkedin_post(self, *, post_title: str, post_content: str):
        print(f">>>> Creating Linkedin Post with title {post_title} in Notion DB")

        page_content = {
            "icon": {
                "emoji": "🤖"
            },
            "parent": {
                "database_id": self.notion_db_id 
            },
            "properties": {
                "Post Title": {
                    "title": [
                        {
                            "text": {
                                "content": post_title
                            }
                        }
                    ]
                },
                "Stage": {
                    "status": {
                        "name": "Generated"
                    }
                },
            },
            "children": [
                {
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": " 📝 Post",
                                },
                            },
                        ],
                        'color': 'red_background'
                    }
                },
                {
                    "object": "block",
                    "type": "code",
                    "code": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": post_content,
                                },
                            },
                        ],
                        "language": "plain text"
                    }
                },
                {
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": " 🎆 Image",
                                },
                            },
                        ],
                        'color': 'green_background'
                    }
                }
            ]
        }

        response = self._send_request(method="POST", path=f"/pages", body=page_content)
        assert response.status_code == 200, f"Failed to create Linkedin post with title {post_title} in Notion DB"

        print(f"<<<< Created Linkedin Post with title {post_title} in Notion DB")