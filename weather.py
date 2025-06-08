import aiohttp
import asyncio
from typing import List, Dict, Optional

async def get_weather(city: str, api_key: str) -> Optional[Dict]:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                data = await response.json()
                
                # Check for API errors
                if response.status != 200:
                    error_msg = data.get('message', 'Unknown API error')
                    print(f"❌ Error for {city}: {error_msg} (Code {response.status})")
                    return None
                
                return {
                    "city": city,
                    "temp": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "description": data["weather"][0]["description"]
                }
    
    except (aiohttp.ClientError, asyncio.TimeoutError, KeyError) as e:
        print(f"⚠️ Failed to fetch weather for {city}: {str(e)}")
        return None

async def get_all_weather(cities: List[str], api_key: str) -> List[Dict]:
    tasks = [get_weather(city, api_key) for city in cities]
    results = await asyncio.gather(*tasks)
    return [result for result in results if result is not None]  # Filter out failures