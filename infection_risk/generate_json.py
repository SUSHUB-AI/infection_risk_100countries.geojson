import json
from datetime import datetime

output = []

# 仮のデータ例（CDC準拠）
countries = [
    {
        "country": "Thailand",
        "iso_code": "TH",
        "diseases": [
            {
                "name": "Dengue Fever",
                "cdc_risk_level": "Watch Level 2",
                "description": "Ongoing outbreak with elevated risk in urban areas.",
                "sources": [
                    "https://wwwnc.cdc.gov/travel/notices/watch/dengue-thailand",
                    "https://www.who.int/news-room/fact-sheets/detail/dengue-and-severe-dengue"
                ]
            }
        ],
        "last_updated": datetime.utcnow().strftime("%Y-%m-%d")
    }
]

with open("cdc_infection_risk_100_countries.json", "w", encoding="utf-8") as f:
    json.dump(countries, f, indent=2, ensure_ascii=False)
