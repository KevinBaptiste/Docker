# 🔐 SSH Key Generator - Interface Graphique

[![Docker](https://img.shields.io/badge/Docker-Supported-blue.svg)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.11-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Application Python avec interface graphique PyQt5 pour générer des clés SSH de manière sécurisée. Compatible Docker pour un déploiement simplifié.

![SSH Key Generator](https://img.shields.io/badge/SSH-Ed25519%20%7C%20RSA-orange)

## ✨ Fonctionnalités

- 🔑 **Génération de clés sécurisées**
  - Ed25519 (recommandé) - Sécurité maximale
  - RSA 2048/4096/8192 bits - Compatibilité universelle
  
- 🛡️ **Protection par passphrase**
  - Chiffrement optionnel de la clé privée
  - Affichage/masquage de la passphrase
  
- 📁 **Gestion flexible**
  - Choix libre de l'emplacement de sauvegarde
  - Ouverture automatique du dossier
  
- 📋 **Copie automatique**
  - Clé publique copiée en un clic
  - Format OpenSSH standard
  
- 🔒 **Sécurité renforcée**
  - Permissions automatiques (600/644)
  - Validation de la passphrase
  
- 🐳 **Support Docker**
  - Déploiement containerisé
  - Mode serverless simple

## 🚀 Installation

### Option 1: Docker (Recommandé)

```bash
# Cloner le dépôt
git clone https://github.com/votre-username/ssh-key-generator.git
cd ssh-key-generator

# Lancer avec Docker
chmod +x docker-run.sh
./docker-run.sh
```

📖 **Documentation complète:** [DOCKER.md](DOCKER.md)

### Option 2: Installation locale

**Prérequis:**
- Python 3.6+
- Linux (Ubuntu, Debian, Fedora, Arch)

**Installation:**

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip python3-pyqt5
pip3 install -r requirements.txt

# Fedora
sudo dnf install python3 python3-pip python3-qt5
pip3 install -r requirements.txt

# Arch Linux
sudo pacman -S python python-pip python-pyqt5
pip3 install -r requirements.txt
```

**Lancement:**

```bash
python3 ssh_key_generator.py
```

## 📖 Utilisation

### Interface graphique

1. **Choisissez le type de clé**
   - Ed25519 (recommandé pour la sécurité)
   - RSA 4096 (recommandé pour la compatibilité)
   - RSA 2048 (compatible universel)

2. **Ajoutez un commentaire**
   - Généralement votre email
   - Aide à identifier la clé

3. **Définissez une passphrase** (fortement recommandé)
   - Protection supplémentaire de la clé privée
   - Demandée à chaque utilisation

4. **Choisissez l'emplacement**
   - Par défaut: `~/.ssh/id_ed25519`
   - Personnalisable selon vos besoins

5. **Générez la clé**
   - Un clic sur le bouton vert
   - Clés créées instantanément

6. **Copiez et utilisez**
   - Copiez la clé publique
   - Ajoutez-la à votre serveur

### Ligne de commande (après génération)

**Copier la clé sur un serveur:**
```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@serveur.com
```

**Ou manuellement:**
```bash
cat ~/.ssh/id_ed25519.pub | ssh user@serveur.com "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

## 🐳 Docker

### docker-compose.yml

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

volumes:
  ssh-keys:
```

### Commandes Docker

```bash
# Construire et lancer
docker compose up --build

# Arrêter
docker compose down

# Voir les logs
docker compose logs -f
```

## 📂 Structure du projet

```
ssh-key-generator/
├── 🐳 Docker
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── docker-run.sh
│   ├── .dockerignore
│   └── DOCKER.md
├── 🐍 Application
│   ├── ssh_key_generator.py
│   └── requirements.txt
├── 📝 Documentation
│   ├── README.md
│   └── interface_preview.html
├── ⚙️ Configuration
│   └── .gitignore
└── 📁 Sortie
    └── generated-keys/
```

## 🔒 Sécurité

### Bonnes pratiques

✅ **Recommandations:**
- Utilisez **toujours** une passphrase forte
- Préférez **Ed25519** pour une sécurité maximale
- **Ne partagez jamais** votre clé privée
- Utilisez des **clés différentes** pour chaque service
- **Sauvegardez** vos clés dans un endroit sûr
- **Renouvelez** vos clés périodiquement

❌ **À éviter:**
- Ne commitez jamais de clés privées sur Git
- N'utilisez pas de passphrase faible
- Ne réutilisez pas la même clé partout

### Permissions automatiques

L'application définit automatiquement:
- **Clé privée:** `600` (rw-------)
- **Clé publique:** `644` (rw-r--r--)

## 📊 Comparaison des types de clés

| Type | Taille | Sécurité | Performance | Compatibilité |
|------|--------|----------|-------------|---------------|
| **Ed25519** | 256 bits | ⭐⭐⭐⭐⭐ | Très rapide | Moderne (OpenSSH 6.5+) |
| **RSA 4096** | 4096 bits | ⭐⭐⭐⭐⭐ | Moyenne | Universelle |
| **RSA 2048** | 2048 bits | ⭐⭐⭐⭐ | Rapide | Universelle |

**Recommandation:** Ed25519 pour la majorité des cas d'usage modernes.

## 🛠️ Dépendances

### Python
- `cryptography` >= 41.0.0 - Génération de clés cryptographiques
- `PyQt5` >= 5.15.0 - Interface graphique

### Système (pour Docker)
- Docker >= 20.10
- Docker Compose >= 1.29
- Serveur X11 (pour l'affichage graphique)

## 🐛 Dépannage

### Problème: Module PyQt5 non trouvé

```bash
pip3 install --user PyQt5
```

### Problème: Module cryptography non trouvé

```bash
pip3 install --user cryptography
```

### Problème: Erreur d'affichage Docker

```bash
xhost +local:docker
export DISPLAY=:0
```

### Problème: Permission refusée

```bash
chmod 700 ~/.ssh
```

Pour plus de détails, consultez [DOCKER.md](DOCKER.md)

## 📸 Aperçu

L'interface inclut:
- Configuration intuitive du type de clé
- Gestion sécurisée des passphrases
- Sélection d'emplacement avec explorateur
- Zone de résultat avec instructions d'utilisation
- Boutons de copie et d'accès rapide

Ouvrez `interface_preview.html` dans votre navigateur pour voir un aperçu.

## 🤝 Contribution

Les contributions sont les bienvenues !

1. Fork le projet
2. Créez votre branche (`git checkout -b feature/AmazingFeature`)
3. Commitez vos changements (`git commit -m 'Add AmazingFeature'`)
4. Push sur la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📝 Roadmap

- [ ] Support de ECDSA
- [ ] Export en différents formats
- [ ] Gestion de trousseau de clés
- [ ] Version web (sans PyQt5)
- [ ] Support Windows via WSL
- [ ] Interface en ligne de commande (CLI)
- [ ] Support de YubiKey/Hardware tokens

## 📜 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👤 Auteur

Créé pour simplifier et sécuriser la génération de clés SSH.

## 🙏 Remerciements

- [Cryptography](https://cryptography.io/) - Bibliothèque cryptographique Python
- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/) - Framework d'interface graphique
- [OpenSSH](https://www.openssh.com/) - Protocole SSH de référence

## 📞 Support

- 🐛 [Signaler un bug](https://github.com/votre-username/ssh-key-generator/issues)
- 💬 [Poser une question](https://github.com/votre-username/ssh-key-generator/discussions)
- 📧 Contact: votre-email@example.com

---

⭐ **Si ce projet vous est utile, n'oubliez pas de mettre une étoile !** ⭐
