import requests


# Example: fetch PC4 boundaries from PDOK
PDOK_URL = "https://geodata.nationaalgeoregister.nl/cbsgebiedsindelingen/wfs?service=WFS&version=2.0.0&request=GetFeature&typeName=cbsgebiedsindelingen:cbs_pc4_2022_gegeneraliseerd&outputFormat=application/json"


if __name__ == "__main__":
r = requests.get(PDOK_URL)
print(r.status_code, len(r.json().get("features", [])))