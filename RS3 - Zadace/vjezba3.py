import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autorizacija(korisnik, lozinka):
    print(f"Započinjem autorizaciju za korisnika {korisnik['korisnicko_ime']}...")
    await asyncio.sleep(2) 
    korisnik_lozinka = next((item for item in baza_lozinka if item['korisnicko_ime'] == korisnik['korisnicko_ime']), None)
    if korisnik_lozinka and korisnik_lozinka['lozinka'] == lozinka:
        return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija uspješna."
    return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija neuspješna."

async def autentifikacija(korisnik):
    print(f"Započinjem autentifikaciju za korisnika {korisnik['korisnicko_ime']}...")
    await asyncio.sleep(3) 
    korisnik_baza = next((item for item in baza_korisnika if item['korisnicko_ime'] == korisnik['korisnicko_ime'] and item['email'] == korisnik['email']), None)
    if not korisnik_baza:
        return f"Korisnik {korisnik['korisnicko_ime']} nije pronađen."
    
    return await autorizacija(korisnik_baza, korisnik['lozinka'])

async def main():
    korisnik = {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com', 'lozinka': 'super_teska_lozinka'}
    rezultat = await autentifikacija(korisnik)
    print(rezultat)



asyncio.run(main())
