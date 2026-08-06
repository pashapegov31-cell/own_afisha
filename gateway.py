import httpx
from fastapi import Request, Response

from main import app

django_url = "http://127.0.0.1:8000/"


@app.api_route(
    "/app/v1/django/{path:path}", methods=["PUT", "GET", "DELETE", "PATCH", "POST"]
)
async def django(path: str, req: Request):

    DJANGO_URL = f"{django_url}app/v1/django/{path}"
    req_headers = dict(req.headers)
    req_headers.pop("host", None)
    req_headers.pop("content-length", None)
    try:
        async with httpx.AsyncClient() as async_client:
            response = await async_client.request(
                method=req.method,
                url=DJANGO_URL,
                headers=req_headers,
                content=await req.body(),
                params=req.query_params,
            )
            return Response(
                status_code=response.status_code,
                content=response.content,
                headers=dict(response.headers),
            )
    except httpx.RequestError:
        return Response(status_code=502, content="Bad Gateway")
