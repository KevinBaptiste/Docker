# Générateur de clés SSH - Version Docker

Application Python avec interface graphique pour générer des clés SSH de manière sécurisée, containerisée avec Docker.

## 🐳 Prérequis

- **Docker** (version 20.10 ou supérieure)
- **Docker Compose** (version 1.29 ou supérieure)
- **Système Linux** avec serveur X11 (pour l'interface graphique)

### Installation de Docker

**Ubuntu/Debian:**
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

**Fedora:**
```bash
sudo dnf install docker docker-compose
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
```

**Arch Linux:**
```bash
sudo pacman -S docker docker-compose
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
```

⚠️ **Important:** Déconnectez-vous et reconnectez-vous après avoir ajouté votre utilisateur au groupe docker.

## 🚀 Utilisation rapide

### Méthode 1: Script automatique (Recommandé)

```bash
# Rendre le script exécutable
chmod +x docker-run.sh

# Lancer l'application
./docker-run.sh
```

### Méthode 2: Commandes Docker Compose manuelles

```bash
# Autoriser l'affichage X11
xhost +local:docker

# Construire et lancer le conteneur
docker compose up --build

# Ou en arrière-plan
docker compose up -d --build

# Arrêter le conteneur
docker compose down

# Nettoyer
xhost -local:docker
```

## 📁 Structure du projet

```
ssh-key-generator/
├── Dockerfile              # Configuration du conteneur Docker
├── docker-compose.yml      # Orchestration Docker (serverless)
├── docker-run.sh           # Script de lancement automatique
├── ssh_key_generator.py    # Application Python principale
├── requirements.txt        # Dépendances Python
├── README.md              # Documentation complète
├── DOCKER.md              # Ce fichier
├── .dockerignore          # Fichiers à exclure du build Docker
├── .gitignore             # Fichiers à exclure de Git
└── generated-keys/        # Dossier pour les clés générées (auto-créé)
```

## 🔑 Récupération des clés générées

Les clés SSH générées sont accessibles de **deux façons** :

### 1. Volume Docker partagé (Recommandé)

Les clés sont automatiquement copiées dans le dossier `generated-keys/` :

```bash
ls -la generated-keys/
# Vous verrez vos clés SSH ici
```

### 2. Volume Docker persistant

Les clés sont également stockées dans un volume Docker nommé `ssh-keys` :

```bash
# Lister les volumes
docker volume ls

# Inspecter le volume
docker volume inspect ssh-key-generator_ssh-keys

# Copier les clés depuis le volume
docker cp ssh-key-generator:/root/.ssh/id_ed25519 ./
docker cp ssh-key-generator:/root/.ssh/id_ed25519.pub ./
```

## ⚙️ Configuration

### Personnaliser le docker-compose.yml

Le fichier `docker-compose.yml` est configuré en mode **serverless** (simple) :

```yaml
version: '3.8'

services:
  ssh-key-generator:
    build: .
    container_name: ssh-key-generator
    environment:
      - DISPLAY=${DISPLAY}
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:rw
      - ssh-keys:/root/.ssh
      - ./generated-keys:/output
    network_mode: host
    restart: unless-stopped
```

**Options personnalisables :**

- `container_name`: Nom du conteneur
- `restart`: Politique de redémarrage (`no`, `always`, `unless-stopped`)
- Volumes: Ajoutez ou modifiez les volumes montés

### Variables d'environnement

Vous pouvez créer un fichier `.env` pour personnaliser :

```bash
# .env
DISPLAY=:0
```

## 🐛 Dépannage

### Problème: "cannot open display"

L'erreur `cannot open display` signifie que Docker ne peut pas accéder à votre serveur X11.

**Solution:**
```bash
# Autoriser l'accès X11
xhost +local:docker

# Vérifier que DISPLAY est défini
echo $DISPLAY

# Exporter DISPLAY si nécessaire
export DISPLAY=:0
```

### Problème: Permission refusée pour /tmp/.X11-unix

**Solution:**
```bash
# Donner les permissions temporaires
sudo chmod 1777 /tmp/.X11-unix

# Ou exécuter avec sudo (non recommandé)
sudo ./docker-run.sh
```

### Problème: Le conteneur se ferme immédiatement

**Solution:**
```bash
# Voir les logs
docker compose logs

# Démarrer en mode interactif pour déboguer
docker compose run --rm ssh-key-generator bash
```

### Problème: "Docker daemon is not running"

**Solution:**
```bash
# Démarrer Docker
sudo systemctl start docker

# Vérifier le statut
sudo systemctl status docker
```

### Problème: Interface graphique floue ou pixelisée

Cela peut être dû à la mise à l'échelle HiDPI.

**Solution:**
```bash
# Ajouter au docker-compose.yml sous environment:
- QT_AUTO_SCREEN_SCALE_FACTOR=0
- QT_SCALE_FACTOR=1
```

## 🔒 Sécurité

### Bonnes pratiques

✅ **À faire:**
- Toujours utiliser une passphrase forte
- Ne jamais partager vos clés privées
- Utiliser le dossier `generated-keys/` uniquement pour la récupération
- Supprimer les clés de test après usage
- Ajouter `generated-keys/` au `.gitignore` (déjà fait)

❌ **À ne pas faire:**
- Ne jamais commit de clés privées sur Git
- Ne jamais exposer le conteneur Docker sur internet
- Ne pas partager le volume Docker `ssh-keys` avec d'autres conteneurs non sécurisés

## 📊 Commandes utiles

```bash
# Voir les conteneurs en cours
docker ps

# Voir tous les conteneurs
docker ps -a

# Arrêter le conteneur
docker compose down

# Supprimer le conteneur et le volume
docker compose down -v

# Reconstruire l'image
docker compose build --no-cache

# Voir les logs en temps réel
docker compose logs -f

# Nettoyer les images Docker non utilisées
docker system prune -a
```

## 🚢 Déploiement sur GitHub

### 1. Initialiser le dépôt Git

```bash
git init
git add .
git commit -m "Initial commit: SSH Key Generator with Docker"
```

### 2. Créer un dépôt sur GitHub

Allez sur https://github.com/new et créez un nouveau dépôt.

### 3. Pousser le code

```bash
git remote add origin https://github.com/votre-username/ssh-key-generator.git
git branch -M main
git push -u origin main
```

### 4. Fichiers à vérifier avant le push

Assurez-vous que ces fichiers sont présents et correctement configurés :
- ✅ `.gitignore` - Pour exclure les clés et fichiers sensibles
- ✅ `.dockerignore` - Pour optimiser le build Docker
- ✅ `README.md` - Documentation principale
- ✅ `DOCKER.md` - Documentation Docker

## 📝 Notes importantes

- Le mode **serverless** signifie que le conteneur se lance, exécute l'application, et s'arrête quand vous fermez l'interface
- Le volume `ssh-keys` persiste même après l'arrêt du conteneur
- L'utilisation de `network_mode: host` permet une configuration X11 simplifiée
- Les clés sont automatiquement copiées dans `generated-keys/` pour un accès facile

## 🆘 Support

En cas de problème :

1. Vérifiez les logs : `docker compose logs`
2. Consultez la section Dépannage ci-dessus
3. Ouvrez une issue sur GitHub avec les logs et votre configuration

## 📜 Licence

Ce projet est libre d'utilisation et de modification.

---

**Créé avec ❤️ pour simplifier la génération de clés SSH**
