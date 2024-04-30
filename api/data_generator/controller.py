from fastapi import APIRouter

from .rag_fusion import getBlog

router = APIRouter(
    prefix= '/data-generator',
    tags= ['data-generator']
)

@router.get('/query/{query}')
def generate_data(query):
    return getBlog(query)