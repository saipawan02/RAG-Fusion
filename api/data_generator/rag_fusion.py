import os
import random
import json

# from config.llm_config import get_completion
from services.chroma_services import getQueryResults

from config.gemini_config import get_completion

def generate_similar_queries(query):
    header = f"""
Generate 4 similar queries related to the below query.
{query}
    """

    footer = """
return the queries in the following JSON format:
{"queries":[generated_queries]}
    """

    query = header + footer
    return json.loads(get_completion(query))

# Mock function to simulate vector search, returning random scores
def vector_search(queries: dict, k: int):
    results = getQueryResults(queries, k)

    queries_res = {}

    for ndx, query in enumerate(queries['queries']):
        if k >len(results['documents'][ndx]):
            k = len(results['documents'][ndx])

        queries_res[query] = []

        for i in range(k):
            document = results['documents'][ndx][i]
            metadata = results['metadatas'][ndx][i]
            score = results['distances'][ndx][i]
            id = results['ids'][ndx][i] 

            queries_res[query].append({
                'document': document,
                'metadata': metadata,
                'score': score,
                'id': id
            })

    return queries_res


# Reciprocal Rank Fusion algorithm
def reciprocal_rank_fusion(search_results_dict, k=60):
    search_results_dict_new = {}
    for key, values in search_results_dict.items():
        search_results_dict_new[key] = {}
        for val in values:
            search_results_dict_new[key][val["document"]] = val["score"]

    fused_scores = {}
    for query, doc_scores in search_results_dict_new.items():
        for rank, (doc, score) in enumerate(sorted(doc_scores.items(), key=lambda x: x[1], reverse = True)):
            if doc not in fused_scores:
                fused_scores[doc] = 0
            previous_score = fused_scores[doc]
            fused_scores[doc] +=1 / (rank + k)
    reranked_results = {doc: score for doc, score in sorted(fused_scores.items(), key=lambda x: x[1], reverse=True)}
    return reranked_results

# Dummy function to simulate generative output
def generate_output(reranked_results, original_query):
    
    header = f"""
Generate a Blog to the query below:
{original_query} 

Also reference the following documents to generate the output:
{reranked_results}
"""

    footer = str("""
So don't use the " inside the blog.                 
return the blog in plain text format with proper heading and sub-heading.
""")

    query = header + footer

    return get_completion(query)

def getBlog(original_query):

    generated_queries = generate_similar_queries(original_query)
    
    search_results = vector_search(generated_queries, 5)
    
    reranked_results = reciprocal_rank_fusion(search_results)
    
    return generate_output(reranked_results, generated_queries)