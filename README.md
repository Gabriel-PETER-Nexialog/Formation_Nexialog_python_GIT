# Module 07 — Coding with IA

> Objectif : apprendre à utiliser les assistants IA dans la génération de code.

---

## Objectifs pédagogiques

- Comprendre le rôle des assistants IA
- Savoir quand et comment les utiliser
- Savoir contrôler et auditer les générations de code
- Savoir planifier et orchestrer l'IA

---

## Prérequis

- Avoir un assistant IA intégré dans son IDE : Claude Code, GitHub Copilot, Codex ou équivalent

---

## Théorie

### Les assistants IA

Les assistants IA sont des outils de programmation directement intégrés dans l'IDE. Ils permettent de :

- **Augmenter la productivité** grâce à la génération et l'autocomplétion de code
- **Créer des prototypes rapidement** pour valider des idées
- **Analyser et comprendre du code legacy** complexe ou volumineux
- **Proposer des solutions alternatives** adaptées au contexte

---

### Bonnes pratiques d'utilisation

#### 1. Écrire le problème avant le code

Avant de solliciter l'IA, rédigez un fichier `plan.md` qui décrit :
- Le problème à résoudre
- Les contraintes connues
- Le comportement attendu

> L'IA génère de meilleures réponses quand le problème est clairement formulé *avant* de demander du code.

---

####  2. Préciser le contexte du projet

Plus le contexte est riche, plus la génération est pertinente. Fournissez systématiquement :

| Élément          | Exemple                                      |
|------------------|----------------------------------------------|
| Langage / stack  | `TypeScript`, `React 18`, `Node 20`          |
| Input / Output   | Type et format des données attendues         |
| Use case concret | Un exemple réel d'utilisation                |
| Contraintes      | Performance, compatibilité, normes internes  |

---

#### 3. Demander un plan avant le code

Avant toute génération, demandez à l'IA de produire un **plan d'implémentation** :

```
Avant de coder, propose-moi un plan étape par étape pour [ta demande].
```

Cela permet de :
- Valider la compréhension de l'IA avant qu'elle génère du code
- Détecter les malentendus tôt
- Garder le contrôle sur l'architecture choisie

---

#### 4. Implémenter de manière incrémentale

Ne demandez jamais l'intégralité d'une fonctionnalité en une seule fois. Procédez par étapes :

1. Générez une première version minimaliste
2. Testez et validez
3. Enrichissez progressivement
4. Répétez

> L'implémentation incrémentale facilite la revue de code et limite les régressions.

---

#### 5. Rédiger de bons prompts

Un bon prompt contient toujours :

- **Le contexte** : quelle est la situation, quel est le projet
- **La tâche précise** : ce que vous attendez exactement
- **Le style souhaité** : conventions de nommage, format de sortie, niveau de verbosité
- **Les exemples** si possible (input → output attendu)


---

#### Ce qu'il ne faut pas faire

Certaines pratiques sont à éviter absolument avec les assistants IA :

-  **Ne pas demander de gros refactors automatiques** — Décomposez les grandes refactorisations en étapes ciblées et validez chacune.
-  **Prudence sur le code à forte complexité métier** — L'IA ne connaît pas vos règles métier implicites ; relisez et testez systématiquement.
-  **Ne pas générer de code critique sans supervision** — Authentification, gestion des permissions, cryptographie : ces parties doivent être rédigées et auditées par un humain.
-  **Ne jamais transmettre de données sensibles** — Clés privées, tokens, mots de passe, données personnelles (RGPD) ne doivent jamais figurer dans vos prompts.

---

### Récapitulatif — Les réflexes à adopter

```
Écrire plan.md avant de coder
Donner le contexte complet (stack, inputs, outputs, use cases)
Demander un plan d'implémentation en premier
Valider chaque étape avant de continuer
Soigner ses prompts (contexte, tâche, style, exemples)
Relire et tester tout code généré
Ne jamais partager de secrets ou données sensibles
```

---
## Exercice 1 — Planifier et implémenter un parser de logs incrémental
 
### Contexte
 
Vous travaillez sur un projet backend Python. Des fichiers de logs applicatifs sont générés quotidiennement au format texte. Votre équipe a besoin d'un script capable d'analyser ces fichiers pour en extraire des statistiques utiles.
 
Exemple de ligne de log :
 
```
2024-03-15 08:42:11 ERROR auth_service Failed login attempt for user: jean.dupont@email.com
2024-03-15 08:43:02 INFO  api_gateway Request processed in 142ms - GET /api/products
2024-03-15 08:43:45 WARN  db_service Connection pool at 85% capacity
```
 
### Objectif
 
Construire un script `log_parser.py` qui :
1. Lit un fichier de log passé en argument
2. Compte le nombre d'occurrences par niveau (`INFO`, `WARN`, `ERROR`)
3. Liste les services distincts rencontrés
4. Affiche un résumé clair dans le terminal
 
---
 
### Étapes à suivre
 
#### Étape 1 — Rédiger le `plan.md` (avant tout code)
 
Créez un fichier `plan.md` et décrivez-y :
- Ce que le script doit faire (inputs, outputs, comportements attendus)
- Les étapes d'implémentation que vous envisagez
- Les cas limites à gérer (fichier vide, ligne malformée, etc.)

 
#### Étape 2 — Rédiger un prompt de qualité
 
En vous appuyant sur votre `plan.md`, rédigez un prompt pour votre assistant IA. Il doit contenir :
 
- Le **contexte** (projet backend Python, format des logs)
- La **tâche précise** (ce que le script doit faire)
- Le **format de sortie attendu** (exemple de résumé terminal)
- Une **contrainte** : utiliser uniquement la bibliothèque standard Python (pas de dépendances externes)
 
Soumettez ce prompt à votre assistant IA et récupérez une première version du code.
 
---
 
#### Étape 3 — Implémenter de manière incrémentale
 
Ne demandez pas tout d'un coup. Procédez ainsi :
 
1. **Itération 1** : Faire fonctionner uniquement la lecture du fichier et l'affichage brut des lignes
2. **Itération 2** : Ajouter le comptage par niveau de log
3. **Itération 3** : Ajouter l'extraction des services distincts
4. **Itération 4** : Mettre en forme le résumé final
 
À chaque itération, testez avant de passer à la suivante.
 
---
 
#### Étape 4 — Auditer le code généré
 
Relisez le code produit par l'IA et répondez à ces questions dans un fichier `audit.md` :
 
- La regex ou le parsing utilisé gère-t-il les lignes malformées ?
- Le script se comporte-t-il correctement sur un fichier vide ?
- Y a-t-il des noms de variables ou fonctions peu lisibles ?
- Y a-t-il du code inutile ou redondant généré par l'IA ?
 
Corrigez les problèmes identifiés — avec ou sans l'aide de l'IA.
 
---
 
### Livrable attendu
 
```
exercice_01/
├── plan.md          # Votre plan rédigé avant le code
├── prompt.md        # Le prompt utilisé avec l'IA
├── log_parser.py    # Le script final
├── audit.md         # Votre revue du code généré
└── sample.log       # Un fichier de log de test que vous aurez créé
```
 
---
 
---
 
## Exercice 2 — Auditer et corriger un code généré défaillant
 
### Contexte
 
Un développeur junior de votre équipe a utilisé un assistant IA pour générer rapidement un script Python. Il vous soumet le code ci-dessous pour revue.
 
Votre mission : **identifier, comprendre et corriger ces problèmes** en utilisant l'IA comme outil d'audit.
 
---
 
### Le code à auditer
 
Créez un fichier `buggy_stats.py` avec le contenu suivant :
 
```python
import json
import os
 
def load_users(filepath):
    f = open(filepath)
    data = json.load(f)
    return data["users"]
 
def compute_stats(users):
    total = len(users)
    ages = [u["age"] for u in users]
    average_age = sum(ages) / len(ages)
    
    active = [u for u in users if u["active"] == True]
    inactive = total - len(active)
    
    premium = []
    for u in users:
        if u["plan"] == "premium":
            premium.append(u["name"])
    
    return {
        "total": total,
        "average_age": average_age,
        "active_count": len(active),
        "inactive_count": inactive,
        "premium_users": premium
    }
 
def display_report(stats):
    print("=== Rapport utilisateurs ===")
    print(f"Total : {stats['total']}")
    print(f"Age moyen : {stats['average_age']}")
    print(f"Actifs : {stats['active_count']} | Inactifs : {stats['inactive_count']}")
    print(f"Utilisateurs premium : {', '.join(stats['premium_users'])}")
 
def main():
    path = "users.json"
    users = load_users(path)
    stats = compute_stats(users)
    display_report(stats)
 
main()
```
 
Et créez un fichier `users.json` pour tester :
 
```json
{
  "users": [
    {"name": "Alice", "age": 32, "active": true, "plan": "premium"},
    {"name": "Bob", "age": 27, "active": false, "plan": "free"},
    {"name": "Clara", "age": 41, "active": true, "plan": "premium"},
    {"name": "David", "active": true, "plan": "free"},
    {"name": "Eva", "age": 29, "active": true, "plan": "premium"}
  ]
}
```
 
---
 
### Étapes à suivre
 
#### Étape 1 — Audit manuel
 
Lisez attentivement le code et listez dans un fichier `audit.md` tous les problèmes que vous repérez. Cherchez notamment :
 
- Les ressources non fermées
- Les cas limites non gérés (données manquantes, liste vide…)
- Les comparaisons non idiomatiques Python
- La lisibilité et les opportunités de simplification
- Le comportement si `users.json` n'existe pas
 
---
 
#### Étape 2 — Audit assisté par l'IA
 
Soumettez le code à votre assistant IA avec ce prompt (à adapter) :
 
```
Tu es un développeur Python senior chargé de faire la revue de code suivant.
Identifie tous les bugs, mauvaises pratiques et problèmes de robustesse.
Pour chaque problème, explique pourquoi c'est un problème et propose une correction.
Ne réécris pas tout le fichier : liste les problèmes un par un.
 
[coller le code ici]
```
 
Comparez les résultats de l'IA avec votre audit manuel :
- L'IA a-t-elle trouvé des choses que vous avez manquées ?
- Avez-vous trouvé des choses que l'IA a manquées ?
- L'IA a-t-elle signalé des faux positifs ?
 
---
 
#### Étape 3 — Corriger le code
 
Corrigez `buggy_stats.py` en appliquant les corrections identifiées. Implémentez-les **une par une**, en testant après chaque correction.
 

---
 
#### Étape 4 — Tester les cas limites
 
Modifiez `users.json` pour tester ces scénarios et vérifiez que votre version corrigée les gère :
 
- [ ] Un utilisateur sans champ `age`
- [ ] Une liste `users` vide
- [ ] Un fichier `users.json` absent
- [ ] Un utilisateur sans champ `plan`
 
---
 
### Livrable attendu
 
```
exercice_02/
├── buggy_stats.py    
├── users.json        
├── audit.md           
├── fixed_stats.py     
└── prompt.md         
```
 
---