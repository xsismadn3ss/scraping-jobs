import requests
from bs4 import BeautifulSoup
import re


class ComputrabajoWebScrapingService:
    def __init__(self) -> None:
        self.base_url = "https://sv.computrabajo.com/"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
        }

    def get_job_offers(self, job_title: str, location: str, page: int = 1):

        # preparar la URL para la búsqueda
        location = location.replace(" ", "-").lower()
        job_title = job_title.replace(" ", "-").lower()
        url = f"{self.base_url}trabajo-de-{job_title}-{location}?p={page}"

        # hacer la solicitud HTTP
        response = requests.get(url=url, headers=self.headers)
        if not response.ok:
            return None

        # crear sopa
        soup = BeautifulSoup(response.text, "html.parser")
        total = soup.find("div", class_="box_title").find("h1", class_="title_page").find("span").text.strip()  # type: ignore
        total_pages = int(total) // 20 + 1
        box_offers = soup.find_all("article", class_="box_offer")
        if not box_offers:
            return None
        # obtener el total de ofertas
        scraped_jobs = []
        for box in box_offers:
            job = self.scrap_job(box)
            if job is not None:
                scraped_jobs.append(job)

        data = {
            "total": int(total),
            "page": page,
            "total_pages": total_pages,
            "job_title": job_title.replace("-", " "),
            "location": location.replace("-", " "),
            "job_offers": scraped_jobs,
        }

        return data

    def scrap_job(self, box):
        title: str = box.find("h2").text.strip()
        company = box.find("p", class_="dFlex vm_fx fs16 fc_base mt5").find("a")
        location = box.find("p", class_="fs16 fc_base mt5").find("span")
        published = box.find("p", class_="fs13")
        miscs = box.find("div", class_="fs13 mt15")
        salary: str = ""
        mode: str = ""

        if miscs is not None:
            miscs = miscs.find_all("span", class_="dIB mr10")
            for misc in miscs:
                if re.search(r"\d+", misc.text.strip()):
                    salary = misc.text.strip()
                else:
                    mode = misc.text.strip()

        return {
            "title": title,
            "company": company.text.strip() if company is not None else "Oculto",
            "location": location.text.strip() if location is not None else None,
            "published": published.text.strip() if published is not None else None,
            "mode": mode,
            "salary": salary,
        }
