import requests
from langchain.tools import tool
crop ="Potato"
state ="Karnataka"
Distirct = "Bangalore"
Mandi_API = "579b464db66ec23bdd0000014bc83b93f0a24250512af686d7f1a9f6"

# @tool
def get_crop_price(crop, state, district):
    url = "https://api.data.gov.in/resource/35985678-0d79-46b4-9ed6-6f13308a1d24"

    params = {
        "api-key":Mandi_API ,
        "format": "json",
        "filters[State]": state,
        "filters[District]": district,
        "filters[Commodity]": crop
    }

    response = requests.get(url, params=params)
    data = response.json()

    if not data.get("records"):
        return "No data found"

    record = data["records"][0]

    return {
    "state": record["State"],
    "crop": record["Commodity"],
    "price_per_quintal": f"₹{record['Modal_Price']}",
    "price_per_kg": f"₹{int(record['Modal_Price'])/100:.2f}"
}


print(get_crop_price("Potato", "Karnataka", "Bangalore"))