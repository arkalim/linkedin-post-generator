# LinkedIn Post Generator
## An app to automate LinkedIn post generation!
The app uses LangChain to send API calls to OpenAI's ChatGPT to generate LinkedIn posts. Generated posts are then saved in a Notion database. The Notion database is also queried to feed the LLM as examples in the prompt (few-shot learning).

# For Nerds

### Running the Docker container locally
You can run the Docker image for the app on your local machine instead of GitHub Actions by using the command below.
```
docker run \
-e OPENAI_API_KEY=<your-openai-api-key> \
-e NOTION_API_KEY=<your-notion-api-key> \
-e NOTION_DB_ID=<your-notion-db-id> \
-e NUM_POSTS=5 \
-e SAMPLE_SIZE=10 \
ghcr.io/arkalim/linkedin-post-generator:v1.0.0
```