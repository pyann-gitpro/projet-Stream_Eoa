
# ETEROA - Découverte de l'île de Rurutu 🌴

Bienvenue dans l'application Streamlit **ETEROA**, un tableau de bord interactif qui met en valeur les richesses de l'île de Rurutu : ses paysages, ses légendes, ses actualités et bien plus encore. Ce projet permet aux habitants et aux visiteurs de découvrir et d'explorer les informations essentielles sur l'île.

---

## Fonctionnalités 🚀

- **Carte Visuelle :** Une carte interactive de Rurutu pour explorer les zones géographiques importantes.
- **Découverte :** Une section dédiée aux paysages, à la faune et à la flore de l'île.
- **Légendes :** Découvrez les mythes et légendes captivantes de Rurutu.
- **Actualités :** Restez informé des événements, festivals et initiatives locales.
- **Statistiques :** Analysez les données sur la population et le tourisme.
- **Carte des Vents :** Une carte interactive affichant les données météorologiques des vents en temps réel.

---

## Structure du Projet 📂

```
streamlit_app/
│
├── app-eoa.py             # Fichier principal de l'application
├── README.md              # Documentation du projet
├── pages/                 # Pages modulaires du projet
│   ├── carte_visuelle.py
│   ├── decouverte.py
│   ├── legendes.py
│   ├── actualites.py
│   ├── statistiques.py
│   ├── carte_des_vents.py
├── public/                # Fichiers statiques (images, etc.)
│   ├── assets/
│       ├── logo_grayscale.png
│       ├── discovers.webp
│       ├── legends.webp
│
├── requirements.txt       # Dépendances Python
```

---

## Installation 💻

### 1. Pré-requis
- [Python 3.8+](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)

### 2. Cloner le projet
```bash
git clone https://github.com/votre-repo/eteroa-app.git
cd eteroa-app
```

### 3. Installer les dépendances
Assurez-vous que toutes les bibliothèques nécessaires sont installées :
```bash
pip install -r requirements.txt
```

### 4. Lancer l'application
Utilisez la commande suivante pour démarrer le serveur Streamlit :
```bash
streamlit run app-eoa.py
```

---

## Usage 🖥️

1. Une fois l'application démarrée, ouvrez le navigateur à l'adresse `http://localhost:8501`.
2. Naviguez à travers les sections via la barre latérale :
   - Explorez les différentes cartes.
   - Découvrez les légendes et les actualités locales.
   - Consultez les statistiques interactives sur la population et le tourisme.

---

## Développement ⚙️

### Ajouter une nouvelle page
1. Créez un fichier Python dans le dossier `pages/`, par exemple `nouvelle_page.py`.
2. Ajoutez une fonction `display_nouvelle_page()` pour définir le contenu de la page.
3. Mettez à jour `app-eoa.py` pour inclure la nouvelle page dans la navigation :
   ```python
   elif options == "Nouvelle Page":
       from pages import nouvelle_page
       nouvelle_page.display_nouvelle_page()
   ```

---

## Dépendances 📦

Les principales bibliothèques utilisées dans ce projet :
- [Streamlit](https://streamlit.io/) : Framework pour créer des applications web interactives.
- [Folium](https://python-visualization.github.io/folium/) : Bibliothèque pour afficher des cartes interactives.
- [Streamlit-Folium](https://github.com/randyzwitch/streamlit-folium) : Intégration de Folium dans Streamlit.
- [Pandas](https://pandas.pydata.org/) : Manipulation et analyse de données.
- [Requests](https://docs.python-requests.org/en/latest/) : Pour interroger les API externes.

---

## Contribution 🤝

Les contributions sont les bienvenues ! Pour proposer des améliorations :
1. Forkez le projet.
2. Créez une branche avec votre fonctionnalité : `git checkout -b feature/nouvelle-feature`.
3. Faites un commit : `git commit -m "Ajout de nouvelle feature"`.
4. Poussez la branche : `git push origin feature/nouvelle-feature`.
5. Ouvrez une Pull Request sur GitHub.

---

## License 📜

Ce projet est sous licence **MIT**. Vous êtes libre de l'utiliser, de le modifier et de le partager.

---

## Auteur 👨‍💻

Développé par [Votre Nom ou Équipe]. Si vous avez des questions, n'hésitez pas à me contacter via [email@example.com](mailto:email@example.com).
