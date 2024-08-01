# Projet brief Docker


1. Pour démarer le projet, utilise la commande docker-compose
```
docker-compose up --build
```

2. Utilise la commande `docker-compose logs jupyter` pour retouver le token pour accéder au Jupyter notebook sur localhost:8887 afin d'utiliser la notebook `insert_data.ipynb` pour ajouter des données de médiathèque dans la base Mongodb 

3. Utiliser Streamlit sur localhost:8501 pour l'analyse

4. On peut égale accéder au mongodb-express en utilisant les infos dans le fichier `.env` sur localhost:8081 pour faire des interations directe avec mongodb-express

5. On peut aussi vérifier si l'api Flask fonction sur localhost:5001