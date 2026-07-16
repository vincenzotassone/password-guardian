import json
from pathlib import Path


class ReportManager:

    def salva_report(self, dati):

        cartella_report = Path(__file__).parent.parent / "reports"
        cartella_report.mkdir(exist_ok=True)

        file_report = cartella_report / "report.json"

        with open(file_report, "w", encoding="utf-8") as file:
            json.dump(dati, file, indent=4)
