import requests


def get_by_bin_stat_egov(bin: str) -> dict:
    data = requests.get(
        url=f"https://old.stat.gov.kz/api/juridical/counter/api/?bin={bin}&lang=en"
    ).json()

    return dat
