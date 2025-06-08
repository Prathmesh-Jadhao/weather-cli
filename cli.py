import asyncio
import argparse
import os
from weather import get_all_weather
from report import create_pdf
from typing import List

async def main(cities: List[str]):
    API_KEY = os.getenv("OWM_API_KEY", "YOUR_DEFAULT_API_KEY")
    
    if API_KEY == "YOUR_DEFAULT_API_KEY":
        print("⚠️ Warning: Using demo API key. Get your own at: https://home.openweathermap.org/api_keys")
    
    weather_data = await get_all_weather(cities, API_KEY)
    
    if weather_data:
        create_pdf(weather_data)
        print(f"✅ Generated report with {len(weather_data)} cities")
    else:
        print("❌ Failed to generate report. No valid data received.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Weather Report Generator')
    parser.add_argument('cities', nargs='+', help='List of cities')
    args = parser.parse_args()
    
    asyncio.run(main(args.cities))