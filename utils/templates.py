IDEA_GENERATION_TEMPLATE = """
You are helping a professional LinkedIn post content writer. He writes short posts on technical topics that interests software engineers. These topics include backend engineering, programming, cloud technologies, cybersecurity, devops principles and tools, AI, Machine Learning, Deep Learning & LLMs. Generate {count} LinkedIn post titles about various technical topics. Since the writer writes short posts, select post titles that can be covered in a short post. Don't select post titles that require a long post for explaining. Each post title should be less than 5 words and should not use cliche words, it should appear intriguing to related technical folks. Make sure to format the output as a list of comma separated items as shown in the examples above. Don't write the output as numbered lists or bullets. Also, the items should not contain any special or escape sequence characters.

Take inspiration from my ideas below (enclosed in examples tag) but don't copy. Generate ideas that are different than the ones below. Introduce other similar ideas.

<examples>
{examples}
</examples>
"""

POST_WRITING_TEMPLATE = """
You are helping a professional LinkedIn post content writer. He writes short posts on technical topics that interests software engineers. These topics include backend engineering, programming, cloud technologies, cybersecurity, devops principles and tools, AI, Machine Learning, Deep Learning & LLMs. Write a short post on the topic "{idea}". Make sure the posts are short and easy to read. Make sure not to write more than 2-3 subtopics and not to write more than 2-3 points per subtopic. Otherwise, the post becomes lengthy. Make sure not to add unnecessary spaces between bullet points or numbered lists.

Take inspiration from my posts below (enclosed in examples tag) but don't copy. Generate content that are different than the ones below.

<examples>
{examples}
</examples>
"""