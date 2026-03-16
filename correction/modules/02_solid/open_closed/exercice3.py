from abc import ABC, abstractmethod

class ExcelManager:
    def write(self, titre, contenu) -> bytes:
        pass

class PdfManager:
    def render(self, titre, contenu) -> bytes:
        pass


class ExporteurRapport(ABC):
    """Interface d'export — fermée à la modification."""
    @abstractmethod
    def exporter(self, sinistre) -> bytes:
        pass


class ExportPDF(ExporteurRapport):
    def exporter(self, sinistre) -> bytes:
        pdf_lib = PdfManager()
        return pdf_lib.render(
            titre="Rapport sinistre",
            contenu=sinistre.description
        )


class ExportExcel(ExporteurRapport):
    def exporter(self, sinistre) -> bytes:
        excel_lib = ExcelManager()
        return excel_lib.write([
            ["ID", sinistre.id],
            ["Montant", sinistre.montant],
        ])


class ExportJSON(ExporteurRapport):
    def exporter(self, sinistre) -> bytes:
        import json
        data = {"id": sinistre.id, "montant": sinistre.montant,
                "description": sinistre.description}
        return json.dumps(data).encode()


class GenerateurRapportSinistre:
    """Ne change jamais, quel que soit le format ajouté."""
    def __init__(self, exporteur: ExporteurRapport):
        self.exporteur = exporteur

    def generer(self, sinistre) -> bytes:
        return self.exporteur.exporter(sinistre)


# Usage
rapport_pdf  = GenerateurRapportSinistre(ExportPDF())
rapport_json = GenerateurRapportSinistre(ExportJSON())