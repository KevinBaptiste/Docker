# 📖 Aide-mémoire - Commandes essentielles

Guide de référence rapide pour toutes les commandes importantes du projet.

## 🐳 Docker

### Commandes de base

```bash
# Construire l'image
docker compose build

# Lancer l'application
docker compose up

# Lancer en arrière-plan
docker compose up -d

# Arrêter
docker compose down

# Arrêter et supprimer les volumes
docker compose down -v

# Voir les logs
docker compose logs -f

# Reconstruire complètement
docker compose build --no-cache

# Redémarrer
docker compose restart
```

### Commandes utiles

```bash
# Voir les conteneurs actifs
docker ps

# Voir tous les conteneurs
docker ps -a

# Entrer dans le conteneur
docker compose exec ssh-key-generator bash

# Voir l'utilisation des ressources
docker stats

# Nettoyer tout
docker system prune -a --volumes
```

### Gestion des volumes

```bash
# Lister les volumes
docker volume ls

# Inspecter un volume
docker volume inspect ssh-key-generator_ssh-keys

# Supprimer un volume
docker volume rm ssh-key-generator_ssh-keys

# Copier depuis un volume
docker cp ssh-key-generator:/root/.ssh/id_ed25519 ./
```

## 🔧 Make (si installé)

```bash
make help        # Afficher toutes les commandes
make build       # Construire l'image
make run         # Lancer l'application
make run-bg      # Lancer en arrière-plan
make stop        # Arrêter
make restart     # Redémarrer
make clean       # Nettoyer
make clean-all   # Nettoyage complet
make logs        # Voir les logs
make shell       # Shell dans le conteneur
make ps          # Status des conteneurs
make rebuild     # Reconstruction complète
make check       # Vérifier les prérequis
make version     # Versions installées
make test-x11    # Tester X11
```

## 🐍 Python (Installation locale)

### Installation

```bash
# Ubuntu/Debian
sudo apt install python3 python3-pip python3-pyqt5
pip3 install -r requirements.txt

# Fedora
sudo dnf install python3 python3-pip python3-qt5
pip3 install -r requirements.txt

# Arch Linux
sudo pacman -S python python-pip python-pyqt5
pip3 install -r requirements.txt

# Avec environnement virtuel
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Lancement

```bash
# Direct
python3 ssh_key_generator.py

# Avec environnement virtuel
source venv/bin/activate
python3 ssh_key_generator.py

# En arrière-plan
nohup python3 ssh_key_generator.py &
```

## 🔑 SSH

### Génération manuelle de clés

```bash
# Ed25519 (recommandé)
ssh-keygen -t ed25519 -C "votre_email@example.com"

# RSA 4096
ssh-keygen -t rsa -b 4096 -C "votre_email@example.com"

# Avec fichier personnalisé
ssh-keygen -t ed25519 -f ~/.ssh/ma_cle -C "commentaire"
```

### Utilisation des clés

```bash
# Copier sur un serveur
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@serveur.com

# Connexion avec clé spécifique
ssh -i ~/.ssh/ma_cle user@serveur.com

# Voir l'empreinte d'une clé
ssh-keygen -lf ~/.ssh/id_ed25519.pub

# Changer la passphrase
ssh-keygen -p -f ~/.ssh/id_ed25519

# Tester la connexion
ssh -T git@github.com
```

### Permissions

```bash
# Corriger les permissions du dossier .ssh
chmod 700 ~/.ssh

# Corriger les permissions de la clé privée
chmod 600 ~/.ssh/id_ed25519

# Corriger les permissions de la clé publique
chmod 644 ~/.ssh/id_ed25519.pub

# Corriger authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

## 🌐 Git & GitHub

### Configuration initiale

```bash
# Configurer Git
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"

# Initialiser le dépôt
git init
git add .
git commit -m "Initial commit"

# Connecter à GitHub
git remote add origin https://github.com/USERNAME/ssh-key-generator.git
git branch -M main
git push -u origin main
```

### Workflow quotidien

```bash
# Voir le statut
git status

# Ajouter des fichiers
git add fichier.py
git add .  # Tous les fichiers

# Commit
git commit -m "Description des changements"

# Push vers GitHub
git push

# Pull depuis GitHub
git pull

# Voir l'historique
git log
git log --oneline
```

### Branches

```bash
# Créer une branche
git checkout -b feature/nouvelle-fonctionnalite

# Changer de branche
git checkout main

# Lister les branches
git branch

# Fusionner une branche
git checkout main
git merge feature/nouvelle-fonctionnalite

# Supprimer une branche
git branch -d feature/nouvelle-fonctionnalite

# Push une branche
git push origin feature/nouvelle-fonctionnalite
```

### Annulations

```bash
# Annuler les modifications non stagées
git checkout -- fichier.py

# Unstage un fichier
git reset HEAD fichier.py

# Modifier le dernier commit
git commit --amend

# Revenir au commit précédent (DANGER)
git reset --hard HEAD~1

# Créer un commit d'annulation
git revert HEAD
```

## 🖥️ X11 / Display

### Configuration X11 pour Docker

```bash
# Autoriser Docker à utiliser X11
xhost +local:docker

# Vérifier DISPLAY
echo $DISPLAY

# Définir DISPLAY si nécessaire
export DISPLAY=:0

# Tester X11
xeyes

# Révoquer l'accès X11
xhost -local:docker
```

### Debug X11

```bash
# Vérifier le serveur X
ps aux | grep X

# Lister les connexions X11
xauth list

# Test avec Docker
docker run --rm -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  alpine:latest sh -c "apk add --no-cache xeyes && xeyes"
```

## 📁 Système de fichiers

### Navigation

```bash
# Lister les fichiers
ls -la

# Trouver un fichier
find . -name "*.py"

# Chercher dans les fichiers
grep -r "texte" .

# Taille d'un dossier
du -sh dossier/

# Espace disque
df -h
```

### Manipulation de fichiers

```bash
# Copier
cp source destination

# Déplacer/Renommer
mv ancien nouveau

# Supprimer
rm fichier
rm -rf dossier/

# Créer un dossier
mkdir -p chemin/vers/dossier

# Permissions
chmod 755 script.sh
chmod +x script.sh
```

## 🔍 Diagnostic

### Vérifier les installations

```bash
# Docker
docker --version
docker compose version

# Python
python3 --version
pip3 --version

# Git
git --version

# Make
make --version
```

### Logs et debug

```bash
# Logs Docker
docker compose logs -f

# Logs Python
python3 -v ssh_key_generator.py

# Processus actifs
ps aux | grep python
ps aux | grep docker

# Ports ouverts
netstat -tulpn
ss -tulpn

# Utilisation mémoire
free -h
```

## 🧹 Nettoyage

### Docker

```bash
# Nettoyer les conteneurs arrêtés
docker container prune

# Nettoyer les images non utilisées
docker image prune -a

# Nettoyer les volumes non utilisés
docker volume prune

# Nettoyer tout
docker system prune -a --volumes
```

### Python

```bash
# Supprimer les caches
find . -type d -name __pycache__ -exec rm -rf {} +
find . -type f -name "*.pyc" -delete
```

### Projet

```bash
# Supprimer les clés générées
rm -rf generated-keys/*

# Supprimer l'environnement virtuel
rm -rf venv/

# Tout réinitialiser
git clean -fdx  # ATTENTION: Supprime tout ce qui n'est pas tracké
```

## ⚡ Raccourcis VS Code

```
Ctrl+`           Ouvrir/fermer le terminal
Ctrl+Shift+P     Palette de commandes
Ctrl+Shift+G     Source Control (Git)
Ctrl+Shift+E     Explorateur de fichiers
Ctrl+B           Basculer la barre latérale
Ctrl+K Ctrl+T    Changer le thème
F5               Déboguer/Lancer
Ctrl+C           Copier
Ctrl+V           Coller
Ctrl+F           Rechercher
Ctrl+H           Remplacer
Ctrl+/           Commenter/décommenter
```

## 📦 Mise à jour des dépendances

```bash
# Voir les dépendances obsolètes
pip list --outdated

# Mettre à jour une dépendance
pip install --upgrade cryptography

# Mettre à jour toutes les dépendances
pip install --upgrade -r requirements.txt

# Geler les versions
pip freeze > requirements.txt
```

## 🎯 Commandes par cas d'usage

### Premier lancement

```bash
git clone https://github.com/USERNAME/ssh-key-generator.git
cd ssh-key-generator
./docker-run.sh
```

### Développement

```bash
git checkout -b feature/ma-feature
# Modifications...
git add .
git commit -m "feat: nouvelle fonctionnalité"
git push origin feature/ma-feature
```

### Mise à jour depuis GitHub

```bash
git pull
docker compose down
docker compose build --no-cache
docker compose up
```

### Dépannage complet

```bash
make clean-all
xhost +local:docker
export DISPLAY=:0
make build
make run
```

---

**💡 Conseil:** Marquez cette page dans vos favoris pour un accès rapide !
