import json
from llama_cpp import Llama
from langchain.embeddings import LlamaCppEmbeddings

embeddings = LlamaCppEmbeddings(model_path="models/mistral-7b-instruct-v0.1.Q3_K_L.gguf", verbose=True, n_ctx=2048)

llm = Llama(
      model_path="models/mistral-7b-instruct-v0.1.Q3_K_L.gguf",
      embedding=True,
      verbose=True, 
      n_ctx=2048
)

def get_completion(original_query):

    response = llm.create_chat_completion(messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that outputs in JSON.",
            },
            {"role": "user", "content": original_query},
        ],
        response_format={
            "type": "json_object",
        },
        temperature=0.7,
    )
    print(response)
    return json.loads(response['choices'][0]['message']['content'].strip())

