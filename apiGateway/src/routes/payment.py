from fastapi import APIRouter, HTTPException
import httpx
from apiGateway.src.config import PAYMENT_API_URL

router = APIRouter()

@router.post("/{userId}/create")
async def create_payment(userId: str, payment_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{PAYMENT_API_URL}/{userId}/create", json=payment_data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@router.get("/payments/{userId}")
async def retrieve_all_payments_ByUserId(userId: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{PAYMENT_API_URL}/payments/{userId}",  timeout=100.0)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()
