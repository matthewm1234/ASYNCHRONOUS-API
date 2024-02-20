from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import httpx


@csrf_exempt
async def retrieve_data(request):
    async with httpx.AsyncClient() as client:
        res1 = await client.get('https://quotable.io/quotes?page=1')
        res2 = await client.get('https://randomuser.me/api')
    api1_data = res1.json()
    api2_data = res2.json()

    combine_result = {
        'quotes': api1_data.get('results'),
        'users': api2_data.get('results')
    }

    return JsonResponse(combine_result)
