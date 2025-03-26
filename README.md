
# RAG Fusion Project
This project creates a RAG application for automated article generation. It scrapes data from the web based on a user-provided article name, storing it in a Chroma vector database for efficient retrieval. A RAG pipeline then uses this database to generate a comprehensive article. Key features include automated scraping, ChromaDB storage, and LLM-powered generation. Built using Python, Langchain, and ChromaDB, the project aims to reduce research time and improve article quality by leveraging online information for automated content creation. Potential benefits include scalability, consistency, and up-to-date information.

### Pre-requisites

1. If you want to use local LLM:
Please create a folder named `models` in the base directory and download `mistral-7b-instruct-v0.1.Q3_K_M.gguf` from https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/tree/main in models folder.

2. If you want to use Genimi Model: 
Please specify Gmini API key in the `config/gemini_config.py` file.

### How to run?

1. Install the dependencies using `pip install -r requirements.txt`
2. Run `python main.py`

The API endpoints can be explored by visiting `localhost:3000/docs` in your web browser.

