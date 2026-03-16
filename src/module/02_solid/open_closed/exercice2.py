class GestionnaireRemise:

    def calculer_remise(self, client) -> float:
        remise = 0.0

        if client.anciennete_ans >= 5:
            remise += 0.05

        if len(client.contrats) >= 3:
            remise += 0.10

        if client.a_parraine:
            remise += 0.03

        return min(remise, 0.20)