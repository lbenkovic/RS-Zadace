import asyncio
import aiohttp
import time

async def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main():
    start_time = time.time()

    tasks = [fetch_users() for _ in range(5)]
    responses = await asyncio.gather(*tasks)

    users = responses[0]

    names = [user['name'] for user in users]
    emails = [user['email'] for user in users]
    usernames = [user['username'] for user in users]

    end_time = time.time()
    execution_time = end_time - start_time

    print("Imena korisnika:", names)
    print("Email adrese korisnika:", emails)
    print("Username korisnika:", usernames)
    print(f"Vrijeme izvođenja programa: {execution_time:.2f} sekundi")

asyncio.run(main())
