from datetime import timedelta, date, datetime
import locale
import requests
from fastapi import APIRouter, status
from starlette.responses import Response

companyCode = "53d8db94-7945-42fd-9742-9bbc71dbe4c1"
locationId = "325957"

router = APIRouter(
    prefix="/almere-afval",
    tags=["almere-afval"],
    responses={404: {"description": "Not found"}},
)

@router.get("/next-pickup")
async def get_nextday_container(response: Response):
    resp = await get_next_pickup()
    data = resp.json()
    locale.setlocale(locale.LC_TIME, "nl_NL.UTF-8")
    if (len(data['dataList']) > 0):
        container = get_container_name(data['dataList'][0]['_pickupTypeText'])
        date = datetime.strptime(data['dataList'][0]['pickupDates'][0], '%Y-%m-%dT%H:%M:%S')
    else:
        container = 'geen'
        date = ''

    response.status_code = status.HTTP_200_OK
    return {"nextContainer": container, "datum": date.strftime('%A %d %B')}


async def get_next_pickup():
    url = 'https://wasteapi.ximmio.com/api/GetCalendar'
    startDate = date.today().strftime("%Y-%m-%d")
    endDate = (date.today() + timedelta(days=14)).strftime("%Y-%m-%d")
    payload = {"companyCode": companyCode, "uniqueAddressID": locationId, "startDate": startDate, "endDate": endDate}
    header = {"Content-type": "application/json",
              "Accept": "*/*"}

    x = requests.post(url, json=payload, headers=header)
    return x

def get_container_name(container_type):
    match container_type:
        case 'GREEN': return "GFT"
        case 'PACKAGES': return "PMD"
        case 'PAPER': return "Papier"
        case 'Grey': return "Restafval"
