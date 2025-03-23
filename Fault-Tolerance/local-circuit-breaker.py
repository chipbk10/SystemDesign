import asyncio
import time
from circuitbreaker import CircuitBreaker
import requests
from fastapi import FastAPI
from aiohttp import ClientSession

app = FastAPI()

# Circuit breaker for API A as a whole
breaker_a = CircuitBreaker(failure_threshold=2, recovery_timeout=20, name="API_A")

# Circuit breakers for downstream APIs
breaker_b = CircuitBreaker(failure_threshold=3, recovery_timeout=30, name="API_B")
breaker_c = CircuitBreaker(failure_threshold=3, recovery_timeout=30, name="API_C")
breaker_d = CircuitBreaker(failure_threshold=3, recovery_timeout=30, name="API_D")

# Simulate heavy work in API A
def heavy_work():
    print("API A performing heavy work...")
    time.sleep(2)  # Simulate 2 seconds of computation
    print("API A heavy work completed.")
    return "Heavy work result"

# Async functions for downstream APIs
@breaker_b
async def call_api_b(session):
    async with session.get("https://api-b.example.com") as response:
        response.raise_for_status()
        return await response.json()

@breaker_c
async def call_api_c(session):
    async with session.get("https://api-c.example.com") as response:
        response.raise_for_status()
        return await response.json()

@breaker_d
async def call_api_d(session):
    async with session.get("https://api-d.example.com") as response:
        response.raise_for_status()
        return await response.json()

# API A’s main logic with its own circuit breaker
@breaker_a
async def api_a_logic():
    # Step 1: Perform heavy work
    heavy_result = heavy_work()

    # Step 2: Call API B, C, D concurrently
    async with ClientSession() as session:
        tasks = [
            call_api_b(session),
            call_api_c(session),
            call_api_d(session)
        ]
        # Gather results; any failure raises an exception
        results = await asyncio.gather(*tasks, return_exceptions=False)

    # Step 3: Combine results
    return {
        "heavy_work": heavy_result,
        "api_b": results[0],
        "api_c": results[1],
        "api_d": results[2]
    }

# FastAPI endpoint
@app.get("/process")
async def process():
    try:
        result = await api_a_logic()
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "message": f"API A failed: {str(e)}"}

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
