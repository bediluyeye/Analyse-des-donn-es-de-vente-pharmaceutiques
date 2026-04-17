import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Chargement et preparation
df = pd.read_csv('data/salesdaily.csv', sep=';')
df['datum'] = pd.to_datetime(df['datum'])
df['year'] = df['datum'].dt.year
df['month'] = df['datum'].dt.month
df['weekday_name'] = df['datum'].dt.day_name()

medicaments = ['M01AB', 'M01AE', 'N02BA', 'N02BE', 'N05B', 'N05C', 'R03', 'R06']

print("ANALYSE COMPLÈTE DES VENTES DE MeDICAMENTS")

# ============================================================================
# QUESTION 1 : Volumes de ventes totaux pour chaque categorie (code ATC)
# ============================================================================
print("\n1. VOLUMES DE VENTES TOTAUX PAR CATeGORIE (CODE ATC)")

q1_volumes = df[medicaments].sum().sort_values(ascending=False)
for med, volume in q1_volumes.items():
    print(f"{med}: {volume:,.2f} unites")

plt.figure(figsize=(10, 6))
q1_volumes.sort_values(ascending=True).plot(kind='barh', color='steelblue', edgecolor='black')
plt.title('Volumes de ventes totaux par categorie ATC')
plt.xlabel('Volume de ventes')
plt.ylabel('Categorie ATC')
plt.tight_layout()
plt.show()

# ============================================================================
# QUESTION 2 : Marques individuelles avec ventes totales les plus elevees
# ============================================================================
print("\n2. MARQUES DE MeDICAMENTS AVEC VENTES TOTALES LES PLUS eLEVeES")
print("-" * 80)
q2_marques = df[medicaments].sum().sort_values(ascending=False)
print("TOP 10 des medicaments:")
for i, (med, volume) in enumerate(q2_marques.head(10).items(), 1):
    print(f"{i}. {med}: {volume:,.2f} unites")

plt.figure(figsize=(10, 6))
q2_marques.head(8).plot(kind='bar', color='coral', edgecolor='black')
plt.title('Top 8 des medicaments par volume total')
plt.ylabel('Volume de ventes')
plt.xlabel('Categorie ATC')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ============================================================================
# QUESTION 3 : Top 3 medicaments en janvier 2015, juillet 2016, septembre 2017
# ============================================================================
print("\n3. TOP 3 MeDICAMENTS PAR PeRIODE")

dates_test = [(2015, 1), (2016, 7), (2017, 9)]
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for idx, (y, m) in enumerate(dates_test):
    filtre = df[(df['year'] == y) & (df['month'] == m)]
    top_3 = filtre[medicaments].sum().sort_values(ascending=False).head(3)
    
    print(f"\nTop 3 - {m}/{y}:")
    for i, (med, vol) in enumerate(top_3.items(), 1):
        print(f"  {i}. {med}: {vol:,.2f} unites")
    
    axes[idx].bar(top_3.index, top_3.values, color='salmon', edgecolor='black')
    axes[idx].set_title(f'Top 3 - {m}/{y}')
    axes[idx].set_ylabel('Volume de ventes')
    axes[idx].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

# ============================================================================
# QUESTION 4 : Quel medicament a ete le plus vendu en 2017
# ============================================================================
print("\n4. MeDICAMENT LE PLUS VENDU EN 2017")
print("-" * 80)
df_2017 = df[df['year'] == 2017]
q4_data = df_2017[medicaments].sum().sort_values(ascending=False)
top_med_2017 = q4_data.index[0]
top_vol_2017 = q4_data.values[0]
print(f"Medicament le plus vendu: {top_med_2017} avec {top_vol_2017:,.2f} unites")
print("\nTop 5 en 2017:")
for i, (med, vol) in enumerate(q4_data.head(5).items(), 1):
    print(f"  {i}. {med}: {vol:,.2f} unites")

plt.figure(figsize=(10, 6))
q4_data.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Ventes totales de medicaments en 2017')
plt.ylabel('Volume de ventes')
plt.xlabel('Categorie ATC')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ============================================================================
# QUESTION 5 : Ventes quotidiennes moyennes par categorie
# ============================================================================
print("\n5. CATeGORIE AVEC VENTES QUOTIDIENNES MOYENNES LES PLUS eLEVeES")

q5_moyennes = df[medicaments].mean().sort_values(ascending=False)
top_cat_q5 = q5_moyennes.index[0]
top_avg_q5 = q5_moyennes.values[0]
print(f"Categorie avec moyenne la plus elevee: {top_cat_q5} avec {top_avg_q5:.2f} unites/jour")
print("\nVentes quotidiennes moyennes pour chaque categorie:")
for med, avg in q5_moyennes.items():
    print(f"  {med}: {avg:.2f} unites/jour")

plt.figure(figsize=(10, 6))
q5_moyennes.sort_values().plot(kind='barh', color='orchid', edgecolor='black')
plt.title('Ventes quotidiennes moyennes par categorie ATC')
plt.xlabel('Moyenne de ventes par jour')
plt.ylabel('Categorie ATC')
plt.tight_layout()
plt.show()

# ============================================================================
# QUESTION 6 : R03 (Respiratoires) davantage vendus certains mois ?
# ============================================================================
print("\n6. ANALYSE MENSUELLE DES MeDICAMENTS RESPIRATOIRES (R03)")
# Aggrege par mois et annee
q6_mensuel = df.groupby(['year', 'month'])['R03'].sum().sort_values(ascending=False)

# Moyennes par mois (toutes annees confondues)
q6_mois_moyen = df.groupby('month')['R03'].sum().sort_values(ascending=False)
mois_noms = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 
             'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Decembre']

print("Ventes R03 par mois (toutes annees):")
for mois, vol in q6_mois_moyen.items():
    print(f"  {mois_noms[mois-1]}: {vol:,.2f} unites")

mois_pic = q6_mois_moyen.idxmax()
vol_pic = q6_mois_moyen.max()
print(f"\nMois avec ventes les plus elevees: {mois_noms[mois_pic-1]} ({vol_pic:,.2f} unites)")

# Visualisation mensuelle
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Graphique 1: Ventes par mois
axes[0].bar(range(1, 13), q6_mois_moyen.values, color='skyblue', edgecolor='black')
axes[0].set_xlabel('Mois')
axes[0].set_ylabel('Volume R03')
axes[0].set_title('Ventes de R03 par mois (total toutes annees)')
axes[0].set_xticks(range(1, 13))
axes[0].set_xticklabels([nm[:3] for nm in mois_noms], rotation=45)
axes[0].grid(axis='y', alpha=0.3)

# Graphique 2: Tendance temporelle
q6_complet = df.groupby('datum')['R03'].sum().reset_index()
axes[1].plot(q6_complet['datum'], q6_complet['R03'].rolling(30).mean(), 
            color='darkblue', linewidth=2, label='Moyenne mobile 30j')
axes[1].scatter(q6_complet['datum'], q6_complet['R03'], alpha=0.3, s=10, color='lightblue', label='Observations')
axes[1].set_xlabel('Date')
axes[1].set_ylabel('Volume R03')
axes[1].set_title('evolution des ventes de R03 (respiratoires) dans le temps')
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()

print("\n" + "="*80)
print("ANALYSE TERMINeE")
print("="*80)

