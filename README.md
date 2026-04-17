# Analyse des Ventes de Médicaments (Classification ATC)

Ce projet propose une analyse statistique et visuelle des données de ventes quotidiennes de médicaments. L'objectif est d'identifier les tendances de consommation, les catégories les plus populaires et les variations saisonnières pour différents groupes thérapeutiques.

## 📋 Description du Projet

Le script traite un jeu de données de ventes pharmaceutiques et répond à six questions clés :
1. **Volumes globaux** : Quelle catégorie ATC domine le marché ?
2. **Top Médicaments** : Quels sont les produits avec les volumes de ventes les plus élevés ?
3. **Analyse Temporelle** : Comparaison des performances sur des mois spécifiques (2015-2017).
4. **Focus Annuel** : Analyse détaillée du leader des ventes pour l'année 2017.
5. **Moyennes Quotidiennes** : Calcul du débit moyen par jour pour chaque catégorie.
6. **Saisonnalité (Groupe R03)** : Étude de l'impact des mois sur les médicaments respiratoires.

## 🛠️ Technologies Utilisées

* **Python 3.x**
* **Pandas** : Manipulation et nettoyage des données.
* **Matplotlib** : Création de visualisations (barres, courbes, nuages de points).
* **NumPy** : Calculs numériques.

## 📊 Structure des Données

Le projet utilise un fichier `data/salesdaily.csv` contenant les colonnes suivantes :
* `datum` : Date de la transaction.
* `M01AB, M01AE, N02BA, N02BE, N05B, N05C, R03, R06` : Volumes de ventes par code ATC.
* Les colonnes de temps (`year`, `month`, `weekday_name`) sont générées dynamiquement par le script.

## 🚀 Installation et Utilisation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/bediluyeye/analyse-pharmacie.git
   cd analyse-pharmacie
   ```

2. **Installer les dépendances** :
   ```bash
   pip install pandas matplotlib numpy scikit-learn
   ```

3. **Lancer l'analyse** :
   ```bash
   python main.py
   ```

## 📈 Exemples de Visualisations

Le script génère plusieurs graphiques interactifs :
* **Histogrammes horizontaux** pour les volumes totaux et moyens.
* **Comparaison multi-fenêtres** (subplots) pour les performances mensuelles.
* **Graphiques mixtes** (nuage de points + moyenne mobile) pour l'analyse des tendances à long terme du groupe R03.

## 📌 Catégories ATC Analysées

| Code | Description |
| :--- | :--- |
| **M01** | Anti-inflammatoires et antirhumatismaux |
| **N02** | Analgésiques (douleurs) |
| **N05** | Psycholeptiques (sommeil/anxiété) |
| **R03** | Médicaments pour maladies respiratoires obstructives |
| **R06** | Antihistaminiques (allergies) |

---
*Projet réalisé dans le cadre d'une étude d'analyse de données de santé.*
