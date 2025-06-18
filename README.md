# RAG
all info related to RAG. Learning, types and code. 
Retrieval-Augmented Generation (RAG). RAG is a method that retrieves relevant information from a knowledge base and appends it to the user's prompt, significantly enhancing the model's response.

- [latest updates](https://github.com/hymie122/RAG-Survey)
- [All-RAG-Techniques](https://github.com/FareedKhan-dev/all-rag-techniques/blob/main/01_simple_rag.ipynb)
- [All-RAG-Techniques](https://github.com/NirDiamant/RAG_Techniques)

# 6 different types of RAG techniqies

## 1. Standard RAG 
combines 2 RAG concepts. a retrival model (search engine) and a generative model (like GTP).
Good : when you need to retive factual information from external source, while would like to maintain creativity of Gen AI . 
Examples: Customer support chat bot. 

## 2. Corrective RAG
in addition to Standard RAG, adds a validation process to make generated response is not just fluent but also factually correct. 
After the initial retrival & generation, the optput is cross check with trusted data set.
e.g. in medical applications the response might be validated aganist medical papaers or clinical guidlines. if any discrepency or inaccuries are foiund, the model corrects them before presenting it. 
Examples: Ideal for Healthcare or legal research where accuracy is paramount, reducing the risk of misInformation 

[research paper](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://arxiv.org/pdf/2401.15884)
[langGraph implementation](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/)

## 3. Speculative RAG 
Explorative approach. Imagine a question with multiple possible interpretation, Speculative RAG generates multiple possible responses. Then ranks them based on relavence and accuracy. 
The model first retrives the relavent documents, then speculates by generating several possible answers, each of the answers is scored using feedback mechanism which could involve comparing thme to additioanl regtruived documents or using a scoring model to determine which is more relavent. once the higest scoring answer is identified, its presented as final anaswer. This type is particualrly useful for ambigious queries situations where there can be multiple correct answers.
Examples: Asking for recomendations or exploring complex topics whith many possible interpretations. 

[Research paper](https://research.google/blog/speculative-rag-enhancing-retrieval-augmented-generation-through-drafting/)
[Implement with transformers](https://www.datacamp.com/tutorial/speculative-rag)
[LangGraph implementation](https://github.com/jjovalle99/Speculative-RAG)


## 4. Fusion RAG
integrating information from multiple sources. is technique is designed for well rounded comprehensive response by combining data from various different documents. in fusion rag the system retrives multiple documents that offers multiple perspectives or cover various aspects of the query, the generative model then sysnthesis this information merging relavatent points of the query into unified response. if there is conflicting information the model resolves by considering additioanl context or the credibility of the sources.
Example: if you are asking about best programming language in 2025, fusing RAG will pull daat from various sources: Blog, posts, Job portals etc. and genrates a balance response which considers all these perspectives. 

## 5. Agentic RAG
In this technique involves AI acting autonmously, with a specific goal in mind, retriving information and making decisions on its own to achieve desired outcome. 
first, the model is given a specific goal like explaining a complex concept or solving a problem, it then automously plans its actions, deciding which information to retrieve and how to use it achieve the goal. The model iterates this process, refining its understanding and actions dynamically. adjusting its strategy with the feedback it gets during the task. 
Example: AI tutor to explain quantam mechanics - Agentic RAG will automomously plan series of steps, retrieve relavent academic papaers or tutorials, breakdown the information, and guide you thru the explanation step by step. 

## 6. Self RAG
Innovative technique allows the model to improve itself overtime by using its own outputs as new datapoints for future retrival. in Self RAG, AI starts by retriving information and generating response like usual, it stores it own generated response in dedicated repository. next time similar query comes up, the model retrives not just from origunal corpus but also from its previous outputs alloing it to build upon its past knowldge. over time self RAG, enables the model to continously refine its answers learning from its own innovations. this makes it powerful in scnerios whnere the model can benefit from continous learning such as customer service bots, personalized tutoring system 

# Steps to implement RAG 
![Flowchart](https://github.com/user-attachments/assets/9bc46662-f180-467b-88ee-017ddd824731)


## 1. Data collection
first gather all the data that is needed for your application. In the case of a customer support chatbot for an electronics company, this can include user manuals, a product database, and a list of FAQs.

- PDF : done
- Word
- Excel/CSV : done
- Vector DB : done
- Websites : done
- Images
- Videos

## 2. Indexing 

#### 2.a Data Chunking
Data chunking is the process of breaking your data down into smaller, more manageable pieces. For instance, if you have a lengthy 100-page user manual, you might break it down into different sections, each potentially answering different customer questions.
This way, each chunk of data is focused on a specific topic. When a piece of information is retrieved from the source dataset, it is more likely to be directly applicable to the user’s query, since we avoid including irrelevant information from entire documents.
This also improves efficiency, since the system can quickly obtain the most relevant pieces of information instead of processing entire documents.

check SematicChunking for different chunking methods and Standard for basic ones. 

#### 2.b Document embeddings
Now that the source data has been broken down into smaller parts, it needs to be converted into a vector representation. This involves transforming text data into embeddings, which are numeric representations that capture the semantic meaning behind text.

In simple words, document embeddings allow the system to understand user queries and match them with relevant information in the source dataset based on the meaning of the text, instead of a simple word-to-word comparison. This method ensures that the responses are relevant and aligned with the user’s query.

#### 2.c Key Concepts

**Vector DB**
- how you make a vector database from your domain-specific, proprietary data. To create your vector database, you convert your data into vectors by running it through an embedding model.
**embedding model** 
- An embedding model is a type of LLM that converts data into vectors: arrays, or groups, of numbers. In the above example, we’re converting user manuals containing the ground truth for operating the latest Volvo vehicle, but your data could be text, images, video, or audio.
  ![Vector DB using Embedding model](https://github.com/user-attachments/assets/e2d8b743-9031-4241-b0fd-5cc71b9a18e1)

#### 2.d Tools, Libraries, Frameworks & Platforms

**Indexing and Enbedding**
[LlamaIndex - git](]https://www.datacamp.com/tutorial/llama-index-adding-personal-data-to-llms)
[Python code for Excel using open AI](https://www.datacamp.com/tutorial/introduction-to-text-embeddings-with-the-open-ai-api) 

**Vector DataBase**
[Pinecode - platform](https://www.pinecone.io/)
[qdrant - platform](https://qdrant.tech/)
[PGVector - Git](https://github.com/pgvector/pgvector)


## 3. Retrieval
When a user query enters the system, it must also be converted into an embedding or vector representation. The same model must be used for both the document and query embedding to ensure uniformity between the two.
Once the query is converted into an embedding, the system compares the query embedding with the document embeddings. It identifies and retrieves chunks whose embeddings are most similar to the query embedding, using measures such as cosine similarity and Euclidean distance.
These chunks are considered to be the most relevant to the user’s query.

### 3.a Keyword Search
Search for keyword in embeddings. check llamaidex example 

### 3.b Semantic Search
All examples implements this. the o/p depends on storing and retival strategy. 

### 3.c Filtering
use llamaIndex lib for storing and filtering s=using metadata.

### 3.d ReRanking
<toDo>

### 3.e cosine similarity
<todo>

## 4.Generation
The retrieved text chunks, along with the initial user query, are fed into a language model. The algorithm will use this information to generate a coherent response to the user’s questions through a chat interface.

## 5.Testing 
How to test RAGS for accuracy and correctness.


Knowldge Graph : https://medium.com/@iamshowkath/understanding-knowledge-graph-stores-a-comprehensive-comparison-d7b9248c1ecd 





Prompt caching 

reranking 

From Scratch : 
https://medium.com/red-buffer/building-retrieval-augmented-generation-rag-from-scratch-74c1cd7ae2c0
https://huggingface.co/blog/ngxson/make-your-own-rag

MS Graph RAG
https://medium.com/@zilliz_learn/graphrag-explained-enhancing-rag-with-knowledge-graphs-3312065f99e1

Contextual Retrival:
https://www.youtube.com/watch?v=tmiBae2goJM
https://www.anthropic.com/news/contextual-retrieval

Alternatives to RAG:
https://www.youtube.com/watch?v=IL2ur4_qMTk&pp=ygUidG9wIHJhZyB0ZWNobmlxdWVzIGluIEFJIGV4cGxhaW5lZA%3D%3D

IMproving RAG:
https://www.youtube.com/watch?v=smGbeghV1JE&pp=ygUidG9wIHJhZyB0ZWNobmlxdWVzIGluIEFJIGV4cGxhaW5lZA%3D%3D

Testing RAG:
https://www.youtube.com/watch?v=5fp6e5nhJRk&pp=ygUidG9wIHJhZyB0ZWNobmlxdWVzIGluIEFJIGV4cGxhaW5lZA%3D%3D
