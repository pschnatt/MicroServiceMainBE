import httpx
from fastapi import APIRouter, HTTPException, Request, Response
from apiGateway.src.config import USER_API_URL
  
router = APIRouter()

@router.post("/register")
async def call_register_user(register_data: dict):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(f"{USER_API_URL}/register", json=register_data)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
        return response.json()

@router.post("/login")
async def call_login_user(login_data: dict, response: Response):
    async with httpx.AsyncClient() as client:
        try:
            res = await client.post(f"{USER_API_URL}/login", json=login_data)
            res.raise_for_status()
            
            if "set-cookie" in res.headers:
                response.headers["set-cookie"] = res.headers["set-cookie"]

        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
        
        return res.json()

@router.get("/verify")
async def call_verify_user(request: Request):
    async with httpx.AsyncClient() as client:
        cookies = request.cookies  
        headers = {"Authorization": request.headers.get("Authorization")}  
        
        try:
            res = await client.get(f"{USER_API_URL}/verify", cookies=cookies)
            res.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
        
        return res.json()
