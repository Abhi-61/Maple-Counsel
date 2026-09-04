# Maple Counsel

**Maple Counsel** is a Retrieval-Augmented Generation (RAG) project designed to explore how large language models can answer Canadian immigration-related questions using a curated knowledge base of official immigration documents.

The project combines document preprocessing, semantic retrieval, prompt rewriting, and local LLM-based response generation to create a conversational question-answering system grounded in retrieved source material.

> **Disclaimer:** Maple Counsel is a learning and research project only. It is not intended for commercial use, does not provide legal advice or legal counsel, and should not be relied upon for immigration or other legal decisions. Always consult official government sources or a qualified legal professional where appropriate.

## Overview

The Maple Counsel pipeline consists of the following stages:

1. **Data Collection and Preprocessing**
2. **Metadata Generation**
3. **Document Chunking**
4. **Embedding Generation**
5. **Vector Storage and Retrieval**
6. **Prompt Rewriting**
7. **Response Generation**
8. **Conversation History Management**

## Data Collection

The knowledge base was manually assembled from official Canadian immigration-related sources, including websites such as:

* Immigration, Refugees and Citizenship Canada (IRCC)
* Canada.ca
* Provincial immigration program websites
* Other official Canadian government and immigration-related sources

Some documents were obtained directly in Markdown format, while others were downloaded as HTML and subsequently converted to Markdown.

Markdown was chosen because its heading structure provides useful natural semantic boundaries for document chunking.

## Metadata Generation

Before chunking, metadata is generated for each source document.

Metadata fields include:

* **Filename** – identifies the original source file.
* **Source** – identifies the organization or website from which the document originated.
* **Effective Date** – helps distinguish currently applicable material from outdated information.
* **Binding Flag** – identifies whether the material should be treated as legally or administratively binding. This can help distinguish authoritative material from non-binding guidance, such as certain jurisprudential or policy guides.
* **Content Hash** – provides a fingerprint of the document contents, making it easier to detect changes when refreshing the knowledge base.

The metadata is retained throughout the ingestion process and attached to each resulting chunk.

## Document Chunking

Documents are divided into smaller sections using Markdown headings.

Markdown headings begin with one or more `#` characters, making them useful boundaries for separating documents into semantically meaningful sections.

Each resulting chunk contains fields such as:

```json
{
  "section": "Section Heading",
  "text": "Contents of the section...",
  "filename": "example.md",
  "source": "Canada.ca",
  "effective_date": "...",
  "binding": true,
  "content_hash": "..."
}
```

The processed chunks and document metadata are stored in JSON/JSONL format for use during the remaining ingestion stages.

## Embedding Generation

Each document chunk is converted into a numerical vector representation using:

**`BAAI/bge-base-en-v1.5`**

This embedding model generates **768-dimensional vectors** representing the semantic meaning of the text.

Embeddings make semantic retrieval possible because text with similar meanings tends to be positioned closer together in the embedding vector space, even when the text does not contain exactly the same words.

`BAAI/bge-base-en-v1.5` was selected as a compromise between retrieval quality and the computational limitations of running the project on local hardware.

## Vector Database

The generated embeddings and their associated document data are stored in **Qdrant**.

A vector database is useful in a RAG system because it is designed to efficiently store, index, and search high-dimensional embedding vectors. Instead of comparing a query against every document manually, the database can search for vectors that are closest to the query embedding and return the most semantically relevant chunks.

Qdrant was selected because it is open source, supports local deployment, provides efficient vector similarity search, and integrates easily with Python.

### Current Retrieval Strategy

Maple Counsel currently performs **dense semantic search** using embeddings.

The user's rewritten query is embedded using the same embedding model, and Qdrant searches for document chunks with the most similar vectors.

While semantic search works well for questions expressed in natural language, immigration documents contain significant amounts of domain-specific terminology, program names, statutory references, and other exact terms.

For this reason, a future version of the project could combine semantic retrieval with a lexical search algorithm such as **BM25**.

## Large Language Model

Maple Counsel uses:

**Qwen3 8B**

The model runs locally through **Ollama**.

Qwen3 8B was selected because it provides relatively strong language understanding and reasoning capabilities while remaining small enough to run on CPU-only hardware, although inference performance is significantly slower without GPU acceleration.

The same model is used for two separate stages of the pipeline:

* Prompt rewriting
* Response generation

## Prompt Rewriting

Before document retrieval, the user's query is passed through an LLM-based prompt rewriting stage.

The goal of this step is to transform conversational questions into clearer, more retrieval-friendly queries.

The rewriting process attempts to:

* Remove unnecessary conversational information.
* Preserve the user's original intent.
* Preserve important constraints and terminology.
* Incorporate relevant conversation context.
* Produce a concise query suitable for semantic retrieval.

For example, a follow-up question such as:

> "What about the requirements for that program?"

may not contain enough information to retrieve the correct documents independently.

Using conversation history, the rewriting stage can transform it into a self-contained query containing the relevant program or subject.

## Retrieval

The rewritten query is encoded using `BAAI/bge-base-en-v1.5`.

The resulting vector is sent to Qdrant, which returns the document chunks with the highest semantic similarity to the query.

These retrieved chunks become the knowledge context supplied to the generation model.

## Response Generation

During generation, Qwen3 8B receives:

* The user's original question.
* The retrieved document chunks.
* Relevant conversation history.
* System instructions controlling how the retrieved information should be used.

The model is instructed to answer using the provided documents rather than relying on outside knowledge.

A relatively low temperature is used to encourage more deterministic responses and reduce unnecessary creativity in a domain where factual consistency is important.

After a response is generated, the user's prompt and the model's response are added to the conversation history.

## Conversation History

Maple Counsel maintains a limited conversation history to support follow-up questions and provide a more natural chatbot experience.

The system retains up to the **10 most recent user-assistant exchanges**.

Conversation history is used during both:

* Prompt rewriting, to resolve conversational references and follow-up questions.
* Response generation, to preserve relevant conversational context.

Limiting the history prevents the context supplied to the model from growing indefinitely.

## Pipeline

When a user submits a question, Maple Counsel performs the following operations:

```text
User Question
     │
     ▼
┌─────────────────────┐
│   Prompt Rewriting  │
│     Qwen3 8B        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Query Embedding     │
│ BGE Base EN v1.5    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Semantic Retrieval  │
│       Qdrant        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Response Generation │
│     Qwen3 8B        │
└──────────┬──────────┘
           │
           ▼
      Final Response
```

In summary:

### 1. Prompt Rewriting

The user's question and relevant chat history are provided to the LLM.

The model rewrites the question into a concise, self-contained query optimized for retrieval.

### 2. Retrieval

The rewritten query is embedded and used to perform semantic similarity search against the Qdrant knowledge base.

The most relevant document chunks are returned.

### 3. Generation

The generation model receives:

* The original user question.
* Retrieved documents.
* Conversation history.
* Instructions restricting its answer to the retrieved context.

The resulting response is returned to the user and the conversation history is updated.

## Potential Improvements

Several improvements are planned or could be explored in future versions of Maple Counsel.

### Hybrid Retrieval

Implement lexical retrieval using an algorithm such as **BM25**.

Semantic search is useful for conceptual similarity, while BM25 can perform particularly well for exact terminology, program names, legal references, and uncommon keywords.

### Reciprocal Rank Fusion

Combine semantic and lexical search results using **Reciprocal Rank Fusion (RRF)**.

A possible future retrieval pipeline could therefore become:

```text
                    ┌── Semantic Search ──┐
User Query ─────────┤                     ├── RRF ── Reranking ── LLM
                    └── BM25 Search ──────┘
```

This would allow the strengths of dense and lexical retrieval to complement each other.

### Reranking

Introduce a dedicated reranking model after initial retrieval.

The reranker could evaluate the smaller set of candidate chunks more precisely before the documents are provided to the generation model.

### Improved Hardware and Models

Run the pipeline on more capable hardware with GPU acceleration.

This would improve inference latency and make it practical to experiment with larger embedding, reranking, and language models.

### Automated Knowledge Base Ingestion

Build an ingestion interface that allows users to upload their own documents and automatically perform:

```text
Upload
  ↓
Metadata Generation
  ↓
Chunking
  ↓
Embedding
  ↓
Vector Database Ingestion
```

This would make the system adaptable to other document collections without manually rebuilding the knowledge base.

### Automated Source Refreshing

The existing document hashes and metadata could also be used as the foundation for automatically detecting updated source material and selectively regenerating only the affected chunks and embeddings.

## Running the Project

### Prerequisites

Ensure that the following are installed:

* Python
* Ollama
* Git

### 1. Clone the Repository

```bash
git clone https://github.com/Abhi-61/Maple-Counsel.git
cd Maple-Counsel
```

### 2. Create a Virtual Environment

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Install Ollama for your operating system from:

https://ollama.com/

### 5. Download Qwen3 8B

Run:

```bash
ollama pull qwen3:8b
```

Verify that the model is available with:

```bash
ollama list
```

### 6. Run Maple Counsel

From the project directory:

```bash
python main.py
```

## Technology Stack

| Component             | Technology            |
| --------------------- | --------------------- |
| Language              | Python                |
| LLM Runtime           | Ollama                |
| Language Model        | Qwen3 8B              |
| Embedding Model       | BAAI/bge-base-en-v1.5 |
| Embedding Dimensions  | 768                   |
| Vector Database       | Qdrant                |
| Current Retrieval     | Dense Semantic Search |
| Document Format       | Markdown              |
| Processed Data Format | JSON / JSONL          |

## Project Status

Maple Counsel is currently an experimental learning project.

The current implementation demonstrates an end-to-end local RAG pipeline consisting of:

```text
Document Collection
       ↓
Metadata
       ↓
Chunking
       ↓
Embeddings
       ↓
Qdrant
       ↓
Prompt Rewriting
       ↓
Semantic Retrieval
       ↓
LLM Generation
```

Future development will primarily focus on improving retrieval quality, reducing inference latency, and making knowledge-base ingestion more automated and extensible.

## Disclaimer

**Maple Counsel is an educational and experimental software project. It is not a legal service and does not provide legal or immigration advice.**

The information generated by the system may be incomplete, outdated, or incorrect. The project should not be used as a substitute for official government information or advice from a qualified immigration or legal professional.

Always verify immigration-related information using authoritative sources before making decisions.
