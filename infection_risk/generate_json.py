import json
from datetime import datetime

def generate_infection_risk_json(output_file):
    diseases_data = [
    {
        "name": "Dengue Fever",
        "cdc_risk_level": "Watch Level 2",
        "description": "Elevated risk in urban and semi-urban areas due to mosquito activity.",
        "sources": [
            "https://wwwnc.cdc.gov/travel/notices/watch/dengue-asia",
            "https://www.who.int/news-room/fact-sheets/detail/dengue-and-severe-dengue"
        ]
    },
    {
        "name": "Malaria",
        "cdc_risk_level": "Alert Level 2",
        "description": "Present in rural areas; recommended to take preventive medication.",
        "sources": [
            "https://wwwnc.cdc.gov/travel/notices/alert/malaria-sub-saharan-africa",
            "https://www.who.int/news-room/fact-sheets/detail/malaria"
        ]
    }
]
    countries = [
    {
        "country": "Thailand",
        "iso_code": "TH"
    },
    {
        "country": "India",
        "iso_code": "IN"
    },
    {
        "country": "Brazil",
        "iso_code": "BR"
    },
    {
        "country": "Indonesia",
        "iso_code": "ID"
    },
    {
        "country": "Kenya",
        "iso_code": "KE"
    },
    {
        "country": "Vietnam",
        "iso_code": "VN"
    },
    {
        "country": "Philippines",
        "iso_code": "PH"
    },
    {
        "country": "Nigeria",
        "iso_code": "NG"
    },
    {
        "country": "Bangladesh",
        "iso_code": "BD"
    },
    {
        "country": "Peru",
        "iso_code": "PE"
    },
    {
        "country": "Country 11",
        "iso_code": "C11"
    },
    {
        "country": "Country 12",
        "iso_code": "C12"
    },
    {
        "country": "Country 13",
        "iso_code": "C13"
    },
    {
        "country": "Country 14",
        "iso_code": "C14"
    },
    {
        "country": "Country 15",
        "iso_code": "C15"
    },
    {
        "country": "Country 16",
        "iso_code": "C16"
    },
    {
        "country": "Country 17",
        "iso_code": "C17"
    },
    {
        "country": "Country 18",
        "iso_code": "C18"
    },
    {
        "country": "Country 19",
        "iso_code": "C19"
    },
    {
        "country": "Country 20",
        "iso_code": "C20"
    },
    {
        "country": "Country 21",
        "iso_code": "C21"
    },
    {
        "country": "Country 22",
        "iso_code": "C22"
    },
    {
        "country": "Country 23",
        "iso_code": "C23"
    },
    {
        "country": "Country 24",
        "iso_code": "C24"
    },
    {
        "country": "Country 25",
        "iso_code": "C25"
    },
    {
        "country": "Country 26",
        "iso_code": "C26"
    },
    {
        "country": "Country 27",
        "iso_code": "C27"
    },
    {
        "country": "Country 28",
        "iso_code": "C28"
    },
    {
        "country": "Country 29",
        "iso_code": "C29"
    },
    {
        "country": "Country 30",
        "iso_code": "C30"
    },
    {
        "country": "Country 31",
        "iso_code": "C31"
    },
    {
        "country": "Country 32",
        "iso_code": "C32"
    },
    {
        "country": "Country 33",
        "iso_code": "C33"
    },
    {
        "country": "Country 34",
        "iso_code": "C34"
    },
    {
        "country": "Country 35",
        "iso_code": "C35"
    },
    {
        "country": "Country 36",
        "iso_code": "C36"
    },
    {
        "country": "Country 37",
        "iso_code": "C37"
    },
    {
        "country": "Country 38",
        "iso_code": "C38"
    },
    {
        "country": "Country 39",
        "iso_code": "C39"
    },
    {
        "country": "Country 40",
        "iso_code": "C40"
    },
    {
        "country": "Country 41",
        "iso_code": "C41"
    },
    {
        "country": "Country 42",
        "iso_code": "C42"
    },
    {
        "country": "Country 43",
        "iso_code": "C43"
    },
    {
        "country": "Country 44",
        "iso_code": "C44"
    },
    {
        "country": "Country 45",
        "iso_code": "C45"
    },
    {
        "country": "Country 46",
        "iso_code": "C46"
    },
    {
        "country": "Country 47",
        "iso_code": "C47"
    },
    {
        "country": "Country 48",
        "iso_code": "C48"
    },
    {
        "country": "Country 49",
        "iso_code": "C49"
    },
    {
        "country": "Country 50",
        "iso_code": "C50"
    },
    {
        "country": "Country 51",
        "iso_code": "C51"
    },
    {
        "country": "Country 52",
        "iso_code": "C52"
    },
    {
        "country": "Country 53",
        "iso_code": "C53"
    },
    {
        "country": "Country 54",
        "iso_code": "C54"
    },
    {
        "country": "Country 55",
        "iso_code": "C55"
    },
    {
        "country": "Country 56",
        "iso_code": "C56"
    },
    {
        "country": "Country 57",
        "iso_code": "C57"
    },
    {
        "country": "Country 58",
        "iso_code": "C58"
    },
    {
        "country": "Country 59",
        "iso_code": "C59"
    },
    {
        "country": "Country 60",
        "iso_code": "C60"
    },
    {
        "country": "Country 61",
        "iso_code": "C61"
    },
    {
        "country": "Country 62",
        "iso_code": "C62"
    },
    {
        "country": "Country 63",
        "iso_code": "C63"
    },
    {
        "country": "Country 64",
        "iso_code": "C64"
    },
    {
        "country": "Country 65",
        "iso_code": "C65"
    },
    {
        "country": "Country 66",
        "iso_code": "C66"
    },
    {
        "country": "Country 67",
        "iso_code": "C67"
    },
    {
        "country": "Country 68",
        "iso_code": "C68"
    },
    {
        "country": "Country 69",
        "iso_code": "C69"
    },
    {
        "country": "Country 70",
        "iso_code": "C70"
    },
    {
        "country": "Country 71",
        "iso_code": "C71"
    },
    {
        "country": "Country 72",
        "iso_code": "C72"
    },
    {
        "country": "Country 73",
        "iso_code": "C73"
    },
    {
        "country": "Country 74",
        "iso_code": "C74"
    },
    {
        "country": "Country 75",
        "iso_code": "C75"
    },
    {
        "country": "Country 76",
        "iso_code": "C76"
    },
    {
        "country": "Country 77",
        "iso_code": "C77"
    },
    {
        "country": "Country 78",
        "iso_code": "C78"
    },
    {
        "country": "Country 79",
        "iso_code": "C79"
    },
    {
        "country": "Country 80",
        "iso_code": "C80"
    },
    {
        "country": "Country 81",
        "iso_code": "C81"
    },
    {
        "country": "Country 82",
        "iso_code": "C82"
    },
    {
        "country": "Country 83",
        "iso_code": "C83"
    },
    {
        "country": "Country 84",
        "iso_code": "C84"
    },
    {
        "country": "Country 85",
        "iso_code": "C85"
    },
    {
        "country": "Country 86",
        "iso_code": "C86"
    },
    {
        "country": "Country 87",
        "iso_code": "C87"
    },
    {
        "country": "Country 88",
        "iso_code": "C88"
    },
    {
        "country": "Country 89",
        "iso_code": "C89"
    },
    {
        "country": "Country 90",
        "iso_code": "C90"
    },
    {
        "country": "Country 91",
        "iso_code": "C91"
    },
    {
        "country": "Country 92",
        "iso_code": "C92"
    },
    {
        "country": "Country 93",
        "iso_code": "C93"
    },
    {
        "country": "Country 94",
        "iso_code": "C94"
    },
    {
        "country": "Country 95",
        "iso_code": "C95"
    },
    {
        "country": "Country 96",
        "iso_code": "C96"
    },
    {
        "country": "Country 97",
        "iso_code": "C97"
    },
    {
        "country": "Country 98",
        "iso_code": "C98"
    },
    {
        "country": "Country 99",
        "iso_code": "C99"
    },
    {
        "country": "Country 100",
        "iso_code": "C100"
    }
]
    today = "2025-08-04"
    json_data = []

    for country in countries:
        json_data.append({
            "country": country["country"],
            "iso_code": country["iso_code"],
            "diseases": diseases_data,
            "last_updated": today
        })

    with open(output_file, "w") as f:
        json.dump(json_data, f, indent=4)

if __name__ == "__main__":
    generate_infection_risk_json("cdc_infection_risk_100_countries.json")
