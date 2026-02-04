#!/bin/bash

echo "======================================"
echo "Lancement du Générateur de clés SSH"
echo "======================================"
echo ""

# Vérifier que Docker est installé
if ! command -v docker &> /dev/null; then
    echo "❌ Docker n'est pas installé."
    echo "Installez Docker: https://docs.docker.com/get-docker/"
    exit 1
fi

# Vérifier que Docker Compose est installé
if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null 2>&1; then
    echo "❌ Docker Compose n'est pas installé."
    echo "Installez Docker Compose: https://docs.docker.com/compose/install/"
    exit 1
fi

# Créer le dossier pour les clés générées s'il n'existe pas
mkdir -p generated-keys

# Autoriser la connexion X11 depuis Docker
echo "Configuration de l'affichage X11..."
xhost +local:docker > /dev/null 2>&1

# Démarrer le conteneur
echo "Démarrage du conteneur Docker..."
echo ""

# Utiliser docker compose ou docker-compose selon la version
if docker compose version &> /dev/null 2>&1; then
    docker compose up --build
else
    docker-compose up --build
fi

# Nettoyer l'autorisation X11 à la sortie
echo ""
echo "Nettoyage..."
xhost -local:docker > /dev/null 2>&1

echo "✅ Application fermée"
