from fastapi import FastAPI
import redis

app = FastAPI()
r = redis.Redis(host='redis', port=6379, db=0)


@app.get("/check_data")
async def check_data(phone: str):
    address = r.get(phone)
    if address:
        return {"address": address.decode()}
    else:
        return {"error": "Address not found"}


@app.post("/write_data")
async def write_data(phone: str, address: str):
    r.set(phone, address)
    return {"status": "Data written successfully"}


@app.put("/write_data")
async def update_data(phone: str, address: str):
    if r.exists(phone):
        r.set(phone, address)
        return {"status": "Data updated successfully"}
    else:
        return {"error": "Data not found"}
