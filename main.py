import requests
from requests.adapters import HTTPAdapter
from decouple import config

from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse


app = FastAPI()


def get_obj() -> list:
    result = []
    
    for _ in range(25):
        session = requests.Session()
        retry = HTTPAdapter(max_retries=5)
        session.mount("http://", retry)
        session.mount("https://", retry)
        r = session.get(config("URL"))
        
        obj = {
            'id':r.json()['id'],
            'value':r.json()['value']
        }
        result.append(obj)
    
    return result

@app.get("/")
def get_endpoint():
    
    result = get_obj()

    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                'array':result
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                'error': 'Internal server error',
                'message': e
            }
        )