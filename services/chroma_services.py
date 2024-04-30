from config.chroma_config import collection, text_splitter


def getQueryResults(queries, k):
    return collection.query(
        query_texts = queries['queries'],
        n_results = k
    )

def splitAndupload(text, file_name, uuid_str, page_num=0):
    documents = text_splitter.split_text(text)
    collection.add(
        documents=documents,
        metadatas = [{"source": f"{file_name}", "page": f"{page_num + 1}"} for num in range(len(documents))],
        ids = [str(uuid_str) + "_" + str(page_num + 1) + "_" + str(num) for num in range(len(documents))]
    )