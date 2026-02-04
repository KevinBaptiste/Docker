FROM python:3.11-slim

# Installer les dépendances système pour PyQt5 et X11
RUN apt-get update && apt-get install -y \
    python3-pyqt5 \
    python3-pyqt5.qtsvg \
    libqt5gui5 \
    libqt5widgets5 \
    libqt5core5a \
    x11-apps \
    xauth \
    && rm -rf /var/lib/apt/lists/*

# Créer le répertoire de travail
WORKDIR /app

# Copier les fichiers requirements
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier l'application
COPY ssh_key_generator.py .
COPY README.md .

# Créer le répertoire pour les clés SSH générées
RUN mkdir -p /root/.ssh && chmod 700 /root/.ssh

# Créer un volume pour persister les clés
VOLUME ["/root/.ssh"]

# Variable d'environnement pour l'affichage X11
ENV DISPLAY=:0

# Rendre le script exécutable
RUN chmod +x ssh_key_generator.py

# Point d'entrée
CMD ["python3", "ssh_key_generator.py"]
