from aiohttp import web
async def get_handler(request):
    proizvodi = [
        {'naziv': 'Mlijeko', 'cijena': 2, 'kolicina': 2},
        {'naziv': 'Kruh', 'cijena': 1.2, 'kolicina': 3},
        {'naziv': 'Margarin', 'cijena': 3, 'kolicina': 2},
    ]
    return web.json_response(proizvodi) 

async def post_handler(request):
    proizvodi = await request.json()
    print(proizvodi)
    proizvodi.append({'naziv': 'Kava', 'cijena': 4, 'kolicina': 3})
    return web.json_response(proizvodi) 

async def get_handler_korisnici(request):
    korisnici = [
        {'ime': 'Ivo', 'godine': 25},
        {'ime': 'Ana', 'godine': 17},
        {'ime': 'Marko', 'godine': 19},
        {'ime': 'Maja', 'godine': 16},
        {'ime': 'Iva', 'godine': 22}
    ]
    punoljetni_korisnici = [korisnik for korisnik in korisnici if korisnik['godine'] > 18]
    return web.json_response(punoljetni_korisnici)

app = web.Application()
app.router.add_get('/proizvodi', get_handler) 
app.router.add_post('/proizvodi', post_handler)
app.router.add_get("/stariji_korisnici", get_handler_korisnici)

web.run_app(app, host='localhost', port=8080)
