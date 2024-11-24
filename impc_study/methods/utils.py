import json
from requests import Request, Session


def query(
    core: str,
    query: dict | None = None,
):

    url = f"http://localhost:8983/solr/{core}/query"

    s = Session()

    request = Request(
        method="POST",
        url=url,
        data=json.dumps(query),
        headers={
            "Content-Type": "application/json",
        },
    )

    request = s.prepare_request(request=request)

    response = s.send(request=request)

    try:
        data = json.loads(s=response.content)
    except:
        data = response.content

    return data
