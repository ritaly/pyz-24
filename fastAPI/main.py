from fastapi import FastAPI, status, Request, Response, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import hashlib

app = FastAPI()
app.counter = 0

class HelloResp(BaseModel):
    msg: str

class Product(BaseModel):
    name : str
    description : str | None = None
    price : float
    code : str
    tax : float | None = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/counter")
def read_root():
    app.counter += 1
    return {"Counter: ": app.counter}

@app.get("/hello/{name}", response_model=HelloResp)
def read_root(name: str):
    return HelloResp(msg=f"Hello {name}!")

@app.post("/add_product", status_code=status.HTTP_201_CREATED)
def add_product(product: Product):
    net_price = product.price
    gross_price = net_price # brutto to netto jeśli nie ma podatku

    if product.tax:
        gross_price = net_price + product.tax

    return {
        'data': product,
        'net_price': net_price,
        'gross_price': gross_price
    }


@app.api_route("/method", methods=["GET", "POST", "DELETE", "PUT"])
def detect_http_method(request: Request):
    method = request.method
    response_data = {'method': method}
    if method == "POST":
        return JSONResponse(content=response_data, status_code=201)
    else:
        return JSONResponse(content=response_data, status_code=200)


@app.get("/auth")
def auth(password: str = Query(None), password_hash: str = Query(None)):
    if password is None or password_hash is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    if password_hash == hashlib.sha512(password.encode()).hexdigest():
        return Response(status_code=204)
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")