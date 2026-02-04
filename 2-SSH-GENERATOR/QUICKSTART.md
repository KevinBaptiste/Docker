# 🚀 Guide de démarrage rapide

Ce guide vous permet de démarrer avec le générateur de clés SSH en moins de 5 minutes.

## ⚡ Méthode 1: Docker (Recommandé)

### Installation et lancement en 3 étapes

```bash
# 1. Cloner le projet
git clone https://github.com/votre-username/ssh-key-generator.git
cd ssh-key-generator

# 2. Lancer avec le script automatique
chmod +x docker-run.sh
./docker-run.sh
```

C'est tout ! L'application s'ouvre avec son interface graphique.

### Alternative: Avec Make

```bash
# Si vous avez make installé
make run
```

## 🐧 Méthode 2: Installation locale

### Ubuntu/Debian

```bash
# Installation
sudo apt update
sudo apt install python3-pip python3-pyqt5
pip3 install -r requirements.txt

# Lancement
python3 ssh_key_generator.py
```

### Fedora

```bash
# Installation
sudo dnf install python3-pip python3-qt5
pip3 install -r requirements.txt

# Lancement
python3 ssh_key_generator.py
```

### Arch Linux

```bash
# Installation
sudo pacman -S python-pip python-pyqt5
pip3 install -r requirements.txt

# Lancement
python3 ssh_key_generator.py
```

## 🔑 Utilisation rapide

1. **Sélectionnez Ed25519** (recommandé)
2. **Ajoutez votre email** dans le champ commentaire
3. **Définissez une passphrase** (optionnel mais recommandé)
4. Cliquez sur **"Générer la clé SSH"**
5. **Copiez la clé publique** avec le bouton prévu
6. **Ajoutez-la à votre serveur:**

```bash
# Méthode automatique
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@serveur.com

# Ou pour GitHub
# Collez la clé publique dans: Settings > SSH and GPG keys > New SSH key
```

## 📦 Récupération des clés (Docker)

Les clés générées sont dans le dossier `generated-keys/` :

```bash
ls -la generated-keys/
# Vous verrez vos clés SSH ici
```

## 🆘 Aide rapide

**Problème d'affichage X11 avec Docker ?**
```bash
xhost +local:docker
```

**Voir les logs Docker ?**
```bash
docker compose logs -f
```

**Arrêter l'application ?**
```bash
docker compose down
# ou Ctrl+C si lancée en premier plan
```

## 📚 Documentation complète

- **Docker:** Voir [DOCKER.md](DOCKER.md)
- **Utilisation complète:** Voir [README.md](README.md)

## 🎯 Commandes Make utiles

```bash
make help      # Afficher toutes les commandes
make run       # Lancer l'application
make stop      # Arrêter l'application
make logs      # Voir les logs
make clean     # Nettoyer
make check     # Vérifier les prérequis
```

---

**Besoin d'aide ?** Ouvrez une [issue](https://github.com/votre-username/ssh-key-generator/issues) sur GitHub.
