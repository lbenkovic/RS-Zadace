import asyncio

async def dohvat_podataka():
    print("Započinjem dohvaćanje podataka...")
    await asyncio.sleep(3)  
    podaci = [x for x in range(1, 11)] 
    print("Podaci dohvaćeni.")
    return podaci

async def main():
    podaci = await dohvat_podataka()
    print(f"Dohvaćeni podaci: {podaci}")


asyncio.run(main())
