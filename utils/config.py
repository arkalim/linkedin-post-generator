IDEA_GENERATION_LLM_TEMP = 0.5
POST_WRITING_LLM_TEMP = 0.5
CTA_MESSAGE = "👊🏼 Follow for more tech snippets!"

EXAMPLE_POST_IDEAS = [
    "What is a Large Language Model (LLM)?",
    "What is a Virtual Machine?",
    "Authentication v/s Authorization",
    "Pitfalls of Parallel Computing",
    "Difference Between PROCESS and THREAD",
    "What is Hashing?",
    "What is Retrieval Augmented Generation (RAG)?",
    "Virtual Machines vs Containers",
    "What is an API?",
    "What are vector databases?"
]

EXAMPLE_POST_CONTENT = [
"""
📌 What is an API?

● An API (Application Programming Interface) is a set of rules and protocols for building and interacting with software applications.
● It defines the methods and data formats that applications can use to communicate with each other.

📌 Why are APIs important?

● Integration: APIs allow different software systems to communicate and work together, enabling integration of third-party services and applications.
● Efficiency: APIs streamline processes by allowing your application to use functionalities provided by external services without having to build them from scratch.
● Flexibility: APIs provide a flexible, modular approach to building software, enabling easier updates and enhancements.

📌 Real World Examples:

● Social media platforms providing APIs for sharing content.
● Payment gateways offering APIs for processing transactions.
● Cloud services using APIs for data storage and retrieval.
""",
"""
📌 Virtual Machines vs Containers

💻 Virtual Machines: Complete Isolation

● VMs are essentially full-fledged emulations of physical computers, each running its own operating system and applications.
● They provide complete isolation by virtualizing the hardware, making them ideal for running entirely different operating systems or configurations on a single physical machine.
● The downside? They can be resource-heavy, as each VM includes not just the application and necessary binaries but the entire OS.

📦 Containers: Lightweight and Efficient

● Containers, on the other hand, are more lightweight. They virtualize the operating system, allowing you to run multiple workloads on a single OS instance.
● They are incredibly efficient in terms of resource usage, as each container shares the host system’s kernel, but runs in isolated user spaces.
● Containers are ideal for microservices and applications where you need to deploy many instances efficiently.

🔍 Key Differences

● Resource Utilization: VMs require more resources compared to containers, which are more lightweight and require less overhead.
● Startup Time: Containers typically start up almost instantly, whereas VMs may take longer because they need to boot up an entire OS.
● Use Cases: VMs are excellent for running multiple different operating systems or for applications that require full isolation. Containers are better suited for microservices, cloud-native applications, and scalable, distributed environments.
""",
"""
↗️ What are Vector Databases?

● Definition: Vector databases are specialized databases designed to efficiently store, manage, and query vector data.
● How They Work: Unlike traditional databases that handle discrete values (like numbers and text), vector databases are adept at managing and querying high-dimensional vector data, often used in machine learning and AI applications.

📈 Why Vector Databases?

● Efficiency in AI and ML: They excel in scenarios where large volumes of complex, unstructured data, like images, audio, and text, are involved — typical in machine learning models.
● Speed and Precision: Vector databases enable faster and more accurate retrieval of data, especially in semantic searches, where you're looking for items most similar to a query item.
""",
"""
🤖 What is a Large Language Model (LLM)?

● Definition: An LLM is a type of artificial intelligence model designed to understand, generate, and work with human language.
● How It Works: These models are trained on vast datasets of text and learn patterns and structures of language, enabling them to predict or generate text based on the input they receive.

🔍 Capabilities of LLMs

● Language Understanding and Generation: LLMs can compose text, answer questions, summarize information, translate languages, and even engage in conversation.
● Contextual Learning: They are adept at understanding context and nuances in language, making their interactions more sophisticated and human-like.

🌍 Why LLMs Matter

● Innovation in Communication: LLMs are revolutionizing how we interact with technology, making it more natural and intuitive.
● Business Applications: From chatbots to content creation, LLMs are transforming customer service, marketing, and more.
● Accessibility: They have the potential to break down language barriers and make information more accessible.
""",
"""
🧠 What is Retrieval-Augmented Generation (RAG)?

● Definition: RAG is an AI technique that combines information retrieval with LLM-based text generation.
● How It Works: Essentially, RAG first retrieves relevant information from a large dataset (like a database or the internet) and then passes this information to to an LLM to generate coherent, contextually appropriate responses.

🔗 RAG's Unique Approach

● Retrieval + Generation: Unlike traditional language models that rely solely on pre-trained data, RAG actively fetches external data relevant to the query before generating a response.
● Dynamic and Contextual: This approach allows RAG models to produce more accurate, informative, and context-aware responses, and prevents hallucination.

🌐 Why RAG Matters

Retrieval-Augmented Generation represents a significant leap in the evolution of AI communication capabilities. It blends the best of both worlds: the ability to pull in vast amounts of relevant data and the skill to weave this information into meaningful responses.
"""
]