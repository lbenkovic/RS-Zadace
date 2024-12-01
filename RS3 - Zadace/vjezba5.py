import asyncio

async def secure_data(podaci):
    print(f"Započinjem enkripciju za: {podaci}")
    await asyncio.sleep(3) 
    enkriptirani_podaci = {
        'prezime': podaci['prezime'],
        'broj_kartice': hash(podaci['broj_kartice']),
        'CVV': hash(podaci['CVV'])
    }
    print(f"Enkripcija završena za: {podaci['prezime']}")
    return enkriptirani_podaci

async def main():
    osjetljivi_podaci = [
        {'prezime': 'Perić', 'broj_kartice': '1234567812345678', 'CVV': '123'},
        {'prezime': 'Anić', 'broj_kartice': '8765432187654321', 'CVV': '456'},
        {'prezime': 'Marić', 'broj_kartice': '1122334455667788', 'CVV': '789'}
    ]
    
    zadaci = [secure_data(podaci) for podaci in osjetljivi_podaci]
    
    rezultati = await asyncio.gather(*zadaci)
    
    for rezultat in rezultati:
        print(rezultat)

asyncio.run(main())
