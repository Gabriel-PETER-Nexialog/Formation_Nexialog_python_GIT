
class PdfManager:
    def render(self, titre, contenu):
        pass

class ExcelManager:
    def write(self, titre, contenu) -> bytes:
        pass

class GenerateurRapportSinistre:

    def __init__(self, sinistre):
        self.sinistre = sinistre

    def exporter(self, format: str):
        if format == "pdf":
            pdf_lib = PdfManager()
            return pdf_lib.render(
                titre="Rapport sinistre",
                contenu=self.sinistre.description
            )
        elif format == "excel":
            excel_lib = ExcelManager()
            return excel_lib.write([
                ["ID", self.sinistre.id],
                ["Montant", self.sinistre.montant],
            ])
        else:
            raise ValueError(f"Format non supporté : {format}")