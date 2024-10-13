from fastapi import APIRouter, HTTPException
import httpx
from apiGateway.src.config import RESTAURANT_API_URL

router = APIRouter()

@router.post("/{userId}/create")
async def create_restaurant(userId: str, restaurant_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{RESTAURANT_API_URL}/{userId}/create", json=restaurant_data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@router.get("/get")
async def retrieve_restaurants():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{RESTAURANT_API_URL}/get",  timeout=100.0)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@router.get("/get/{restaurantId}")
async def retrieve_restaurant_by_id(restaurantId: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{RESTAURANT_API_URL}/get/{restaurantId}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@router.put("/{userId}/update/{restaurantId}")
async def update_restaurant(userId: str, restaurantId: str, restaurant_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{RESTAURANT_API_URL}/{userId}/update/{restaurantId}", json=restaurant_data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@router.delete("/{userId}/delete/{restaurantId}")
async def delete_restaurant(userId: str, restaurantId: str):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{RESTAURANT_API_URL}/{userId}/delete/{restaurantId}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()
