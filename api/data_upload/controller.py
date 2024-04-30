import uuid
import requests

from newspaper import Article

from fastapi import APIRouter

from services.chroma_services import splitAndupload


router = APIRouter(
    prefix= '/data-upload',
    tags= ['data-upload']
)

@router.get('/web/')
def scrape_data(url: str):
    uuid_str = str(uuid.uuid4())


    article = Article(url, language="en")

    try:
        article.build()
    except:
        html = requests.get(url, verify=False).text
        article.download(input_html=html)
        article.parse()
        article.nlp()

    text = article.text

    print(text)

    splitAndupload(text, file_name=url, uuid_str=uuid_str)

    return {'uuid': uuid_str, 'message': "success"}