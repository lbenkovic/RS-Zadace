import asyncio

async def dohvat_korisnika():
    print("Započinjem dohvaćanje korisnika...")
    await asyncio.sleep(3)  
    korisnici = [{"id": 1, "ime": "Ana"}, {"id": 2, "ime": "Marko"}, {"id": 3, "ime": "Ivana"}]
    print("Podaci o korisnicima dohvaćeni.")
    return korisnici

async def dohvat_proizvoda():
    print("Započinjem dohvaćanje proizvoda...")
    await asyncio.sleep(5)
    proizvodi = [{"id": 101, "naziv": "Laptop"}, {"id": 102, "naziv": "Telefon"}, {"id": 103, "naziv": "Monitor"}]
    print("Podaci o proizvodima dohvaćeni.")
    return proizvodi

async def main():
    print("Započinjem paralelno dohvaćanje podataka...")
    korisnici, proizvodi = await asyncio.gather(dohvat_korisnika(), dohvat_proizvoda())
    print("Dohvaćanje završeno.")
    print(f"Korisnici: {korisnici}")
    print(f"Proizvodi: {proizvodi}")


asyncio.run(main())
