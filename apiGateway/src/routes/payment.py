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

@router.get("/payments")
async def retrieve_all_payments():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{PAYMENT_API_URL}/payments",  timeout=100.0)
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

@router.get("/payments/singlePayment/{paymentId}")
async def retrieve_single_payment_ByUserId(paymentId: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{PAYMENT_API_URL}/payments/singlePayment/{paymentId}",  timeout=100.0)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@router.get("/account/{paymentId}")
async def retrieve_account_ByPaymentId(paymentId: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{PAYMENT_API_URL}/account/{paymentId}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@router.put("/{paymentId}/update/")
async def update_payment(paymentId: str, payment_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{PAYMENT_API_URL}/{paymentId}/update/", json=payment_data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@router.delete("/{userId}/delete/{paymentId}")
async def delete_payment(userId: str, paymentId: str):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{PAYMENT_API_URL}/{userId}/delete/{paymentId}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()
