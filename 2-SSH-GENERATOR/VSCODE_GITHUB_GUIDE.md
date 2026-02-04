# 📋 Guide d'intégration VS Code et GitHub

Ce guide explique comment intégrer ce projet dans VS Code et le pousser sur GitHub.

## 📁 Structure du projet téléchargé

```
ssh-key-generator/
├── .dockerignore           # Fichiers exclus du build Docker
├── .env.example            # Exemple de configuration environnement
├── .gitignore              # Fichiers exclus de Git
├── Dockerfile              # Configuration du conteneur Docker
├── docker-compose.yml      # Orchestration Docker (serverless)
├── docker-run.sh           # Script de lancement automatique
├── LICENSE                 # Licence MIT
├── Makefile                # Commandes simplifiées
├── README.md               # Documentation principale
├── DOCKER.md               # Documentation Docker détaillée
├── QUICKSTART.md           # Guide de démarrage rapide
├── requirements.txt        # Dépendances Python
├── ssh_key_generator.py    # Application Python principale
└── interface_preview.html  # Aperçu de l'interface
```

## 🚀 Étape 1: Ouvrir dans VS Code

### Option A: Glisser-déposer
1. Téléchargez et extrayez le dossier `ssh-key-generator`
2. Glissez-déposez le dossier dans VS Code

### Option B: Menu Fichier
1. VS Code → Fichier → Ouvrir le dossier
2. Sélectionnez le dossier `ssh-key-generator`

### Option C: Terminal
```bash
cd /chemin/vers/ssh-key-generator
code .
```

## 📦 Étape 2: Extensions VS Code recommandées

VS Code vous proposera d'installer ces extensions:

- **Python** (Microsoft) - Support Python
- **Docker** (Microsoft) - Support Docker
- **GitLens** (GitKraken) - Amélioration Git
- **YAML** (Red Hat) - Support YAML pour docker-compose

Pour installer manuellement:
1. Ctrl+Shift+X (Cmd+Shift+X sur Mac)
2. Recherchez et installez les extensions ci-dessus

## 🔧 Étape 3: Configuration initiale

### 3.1 Créer un fichier .env (optionnel)

```bash
# Dans VS Code, créez un fichier .env à la racine
cp .env.example .env
```

Éditez `.env` si nécessaire (généralement pas besoin).

### 3.2 Vérifier les permissions

Si vous êtes sur Linux/Mac, vérifiez que le script est exécutable:

```bash
chmod +x docker-run.sh
```

## 🐙 Étape 4: Initialiser Git

### 4.1 Initialiser le dépôt local

Dans le terminal intégré de VS Code (Ctrl+`):

```bash
git init
git add .
git commit -m "Initial commit: SSH Key Generator with Docker"
```

### 4.2 Créer un dépôt sur GitHub

1. Allez sur https://github.com/new
2. Nom du dépôt: `ssh-key-generator`
3. Description: `Application Python avec interface graphique pour générer des clés SSH`
4. **NE PAS** cocher "Initialize with README" (on en a déjà un)
5. Cliquez sur "Create repository"

### 4.3 Connecter le dépôt local à GitHub

GitHub vous donnera des commandes. Utilisez celles-ci dans le terminal VS Code:

```bash
git remote add origin https://github.com/VOTRE-USERNAME/ssh-key-generator.git
git branch -M main
git push -u origin main
```

**Authentification requise:**
- Username: votre nom d'utilisateur GitHub
- Password: utilisez un **Personal Access Token** (pas votre mot de passe)

**Pour créer un token:**
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token
3. Sélectionnez `repo` (accès complet)
4. Copiez le token généré

## ✅ Étape 5: Vérification

### 5.1 Vérifier sur GitHub

Allez sur `https://github.com/VOTRE-USERNAME/ssh-key-generator`

Vous devriez voir tous vos fichiers, et le README.md s'affiche automatiquement.

### 5.2 Vérifier le badge

Le README inclut des badges pour:
- Docker Support
- Python Version
- License

## 🔄 Workflow Git dans VS Code

### Interface graphique

VS Code a une interface Git intégrée (icône sur le côté gauche):

1. **Voir les changements:** Icône Source Control (Ctrl+Shift+G)
2. **Stage les fichiers:** Cliquez sur le "+"
3. **Commit:** Écrivez un message et cliquez sur "✓"
4. **Push:** Cliquez sur "..." → Push

### Ligne de commande

```bash
# Voir le statut
git status

# Ajouter les changements
git add .

# Commit
git commit -m "Description des changements"

# Push vers GitHub
git push

# Pull depuis GitHub
git pull
```

## 🐳 Étape 6: Tester Docker localement

Avant de pousser, testez que Docker fonctionne:

```bash
# Avec le script
./docker-run.sh

# Ou avec Make
make run

# Ou manuellement
docker compose up --build
```

## 📝 Personnalisation pour GitHub

### Modifier le README.md

Remplacez dans `README.md`:
- `votre-username` par votre nom d'utilisateur GitHub
- `votre-email@example.com` par votre email
- Ajoutez des captures d'écran si vous le souhaitez

### Ajouter des badges personnalisés

Dans `README.md`, vous pouvez ajouter d'autres badges:

```markdown
[![GitHub Stars](https://img.shields.io/github/stars/VOTRE-USERNAME/ssh-key-generator?style=social)](https://github.com/VOTRE-USERNAME/ssh-key-generator)
[![GitHub Forks](https://img.shields.io/github/forks/VOTRE-USERNAME/ssh-key-generator?style=social)](https://github.com/VOTRE-USERNAME/ssh-key-generator)
```

## 🎨 Bonnes pratiques

### Commits

Utilisez des messages de commit clairs:
- ✅ `feat: add RSA 8192 support`
- ✅ `fix: correct passphrase validation`
- ✅ `docs: update Docker installation guide`
- ❌ `update` (trop vague)
- ❌ `fix bug` (pas assez descriptif)

### Branches

Pour les nouvelles fonctionnalités:

```bash
git checkout -b feature/nom-feature
# Faites vos modifications
git add .
git commit -m "feat: description"
git push origin feature/nom-feature
```

Puis créez une Pull Request sur GitHub.

## 🔒 Sécurité

### Fichiers à NE JAMAIS commit

Le `.gitignore` protège déjà:
- ✅ Clés SSH générées (*.pem, id_rsa, etc.)
- ✅ Variables d'environnement (.env)
- ✅ Dossier `generated-keys/`
- ✅ Caches Python (__pycache__)

### Vérification avant push

```bash
# Voir ce qui sera pushé
git status

# Vérifier qu'aucune clé n'est listée
git ls-files | grep -E "id_rsa|id_ed25519|\.pem$"
# Ne doit rien retourner
```

## 🆘 Problèmes courants

### "Permission denied" lors du push

Utilisez un Personal Access Token au lieu du mot de passe.

### "fatal: remote origin already exists"

```bash
git remote remove origin
git remote add origin https://github.com/VOTRE-USERNAME/ssh-key-generator.git
```

### Fichiers non trackés

```bash
git status
# Ajoutez les fichiers manquants
git add nom-du-fichier
git commit -m "add: missing file"
git push
```

## 📚 Ressources

- [Documentation Git](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com)
- [VS Code Git Support](https://code.visualstudio.com/docs/editor/versioncontrol)
- [Docker Docs](https://docs.docker.com)

## ✨ Prochaines étapes

Une fois sur GitHub:

1. **Ajoutez un screenshot** dans le README
2. **Créez des releases** pour les versions stables
3. **Activez GitHub Actions** pour CI/CD (optionnel)
4. **Ajoutez des issues templates**
5. **Créez une documentation Wiki**

---

**Bon développement ! 🚀**
