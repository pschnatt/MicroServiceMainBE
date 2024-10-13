from fastapi import APIRouter, HTTPException
import httpx
from apiGateway.src.config import BOOKING_API_URL

router = APIRouter()

@router.post("/{userId}/{restaurantId}/create")
async def create_booking(userId: str, restaurantId: str, booking_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BOOKING_API_URL}/{userId}/{restaurantId}/create", json=booking_data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@router.get("/get/restaurantId/{restaurantId}")
async def retrieve_booking_by_restaurantId(restaurantId: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BOOKING_API_URL}/get/restaurantId/{restaurantId}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@router.get("/get/userId/{userId}")
async def retrieve_booking_by_userId(userId: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BOOKING_API_URL}/get/userId/{userId}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@router.get("/get/bookingId/{bookingId}")
async def retrieve_booking_by_id(bookingId: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BOOKING_API_URL}/get/bookingId/{bookingId}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@router.get("/get/date")
async def retrieve_booking_by_date(booking_date_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BOOKING_API_URL}/get/date", json=booking_date_data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@router.delete("/{userId}/cancel/{bookingId}")
async def cancel_booking(userId: str, bookingId: str):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BOOKING_API_URL}/{userId}/cancel/{bookingId}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@router.put("/{userId}/update/{bookingId}")
async def update_booking(userId: str, bookingId: str, booking_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{BOOKING_API_URL}/{userId}/update/{bookingId}", json=booking_data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()