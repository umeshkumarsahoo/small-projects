import requests as req
parameters={
    "amount":10,
    "type":"boolean"
}
response=req.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()
question_data=response.json()["results"]
