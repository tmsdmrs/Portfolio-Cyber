# Analyseur de Logs SSH (SOC / Défense)

## Description
Outil écrit en Python permettant d'analyser un fichier journal d'authentification SSH (`auth.log`), d'extraire automatiquement les adresses IP sources des tentatives échouées et d'identifier les attaques par force brute.

## Démonstration
![Rapport d'analyse de logs SSH](assets/demo-output.png)


## Fonctionnalités
- Parsing de journaux système via expressions régulières (Regex).
- Agrégation et comptage des échecs d'authentification par adresse IP.
- Classification dynamique selon un seuil de suspicion (Alerte à partir de 3 échecs).

## Exécution
```bash
python3 log_analyzer.py
