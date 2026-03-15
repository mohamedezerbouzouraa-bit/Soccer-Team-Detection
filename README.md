# Soccer-Team-Detection

Détection et classification automatique des joueurs de football en équipes Blue et White à partir d’images. Utilise YOLOv8 pour la détection de personnes et analyse uniquement le torse pour identifier la couleur dominante du maillot. Génère l’image annotée avec les scores et compte les joueurs par équipe.

## Installation
pip install -r requirements.txt

## Usage
1. Placez vos images dans `data/sample_images/`.
2. Exécutez `src/detect_players.py`.
3. Les images annotées seront enregistrées dans `outputs/annotated_images/`.
