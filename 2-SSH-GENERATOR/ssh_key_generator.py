#!/usr/bin/env python3
"""
Générateur de clés SSH avec interface graphique
Nécessite: PyQt5, cryptography
"""

import sys
import os
from pathlib import Path
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QComboBox, QTextEdit, QFileDialog, QMessageBox,
                             QGroupBox, QCheckBox, QSpinBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, ed25519
from cryptography.hazmat.backends import default_backend
import subprocess


class SSHKeyGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Générateur de clés SSH")
        self.setGeometry(100, 100, 800, 700)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Titre
        title = QLabel("Générateur de clés SSH")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)
        
        # Configuration de la clé
        config_group = QGroupBox("Configuration de la clé")
        config_layout = QVBoxLayout()
        
        # Type de clé
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("Type de clé:"))
        self.key_type_combo = QComboBox()
        self.key_type_combo.addItems(["Ed25519 (Recommandé)", "RSA 4096", "RSA 2048"])
        self.key_type_combo.currentIndexChanged.connect(self.on_key_type_changed)
        type_layout.addWidget(self.key_type_combo)
        type_layout.addStretch()
        config_layout.addLayout(type_layout)
        
        # Taille de clé RSA (désactivé pour Ed25519)
        size_layout = QHBoxLayout()
        size_layout.addWidget(QLabel("Taille (bits):"))
        self.key_size_spin = QSpinBox()
        self.key_size_spin.setMinimum(2048)
        self.key_size_spin.setMaximum(8192)
        self.key_size_spin.setValue(4096)
        self.key_size_spin.setSingleStep(1024)
        self.key_size_spin.setEnabled(False)
        size_layout.addWidget(self.key_size_spin)
        size_layout.addStretch()
        config_layout.addLayout(size_layout)
        
        # Email/Commentaire
        email_layout = QHBoxLayout()
        email_layout.addWidget(QLabel("Commentaire/Email:"))
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("votre_email@example.com")
        email_layout.addWidget(self.email_input)
        config_layout.addLayout(email_layout)
        
        # Passphrase
        passphrase_layout = QHBoxLayout()
        passphrase_layout.addWidget(QLabel("Passphrase:"))
        self.passphrase_input = QLineEdit()
        self.passphrase_input.setEchoMode(QLineEdit.Password)
        self.passphrase_input.setPlaceholderText("Optionnel mais recommandé")
        passphrase_layout.addWidget(self.passphrase_input)
        config_layout.addLayout(passphrase_layout)
        
        # Confirmation passphrase
        confirm_layout = QHBoxLayout()
        confirm_layout.addWidget(QLabel("Confirmer:"))
        self.confirm_passphrase_input = QLineEdit()
        self.confirm_passphrase_input.setEchoMode(QLineEdit.Password)
        confirm_layout.addWidget(self.confirm_passphrase_input)
        config_layout.addLayout(confirm_layout)
        
        # Afficher passphrase
        self.show_passphrase_check = QCheckBox("Afficher la passphrase")
        self.show_passphrase_check.stateChanged.connect(self.toggle_passphrase_visibility)
        config_layout.addWidget(self.show_passphrase_check)
        
        config_group.setLayout(config_layout)
        main_layout.addWidget(config_group)
        
        # Emplacement de sauvegarde
        location_group = QGroupBox("Emplacement de sauvegarde")
        location_layout = QVBoxLayout()
        
        path_layout = QHBoxLayout()
        path_layout.addWidget(QLabel("Chemin:"))
        self.path_input = QLineEdit()
        default_path = str(Path.home() / ".ssh" / "id_ed25519")
        self.path_input.setText(default_path)
        path_layout.addWidget(self.path_input)
        
        browse_btn = QPushButton("Parcourir...")
        browse_btn.clicked.connect(self.browse_path)
        path_layout.addWidget(browse_btn)
        location_layout.addLayout(path_layout)
        
        location_group.setLayout(location_layout)
        main_layout.addWidget(location_group)
        
        # Bouton de génération
        generate_btn = QPushButton("Générer la clé SSH")
        generate_btn.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-size: 14px; padding: 10px; }")
        generate_btn.clicked.connect(self.generate_key)
        main_layout.addWidget(generate_btn)
        
        # Zone de résultat
        result_group = QGroupBox("Résultat")
        result_layout = QVBoxLayout()
        
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setMinimumHeight(200)
        result_layout.addWidget(self.result_text)
        
        # Boutons d'action
        action_layout = QHBoxLayout()
        
        copy_public_btn = QPushButton("Copier la clé publique")
        copy_public_btn.clicked.connect(self.copy_public_key)
        action_layout.addWidget(copy_public_btn)
        
        open_folder_btn = QPushButton("Ouvrir le dossier")
        open_folder_btn.clicked.connect(self.open_folder)
        action_layout.addWidget(open_folder_btn)
        
        result_layout.addLayout(action_layout)
        result_group.setLayout(result_layout)
        main_layout.addWidget(result_group)
        
        # Variables pour stocker les clés générées
        self.generated_public_key = None
        self.generated_key_path = None
        
    def on_key_type_changed(self, index):
        """Active/désactive la sélection de taille selon le type de clé"""
        key_type = self.key_type_combo.currentText()
        if "Ed25519" in key_type:
            self.key_size_spin.setEnabled(False)
            default_path = str(Path.home() / ".ssh" / "id_ed25519")
        else:
            self.key_size_spin.setEnabled(True)
            default_path = str(Path.home() / ".ssh" / "id_rsa")
        self.path_input.setText(default_path)
    
    def toggle_passphrase_visibility(self, state):
        """Affiche/masque la passphrase"""
        if state == Qt.Checked:
            self.passphrase_input.setEchoMode(QLineEdit.Normal)
            self.confirm_passphrase_input.setEchoMode(QLineEdit.Normal)
        else:
            self.passphrase_input.setEchoMode(QLineEdit.Password)
            self.confirm_passphrase_input.setEchoMode(QLineEdit.Password)
    
    def browse_path(self):
        """Ouvre un dialogue pour choisir l'emplacement"""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Choisir l'emplacement de la clé",
            str(Path.home() / ".ssh"),
            "Tous les fichiers (*)"
        )
        if file_path:
            self.path_input.setText(file_path)
    
    def generate_key(self):
        """Génère la paire de clés SSH"""
        try:
            # Vérifications
            passphrase = self.passphrase_input.text()
            confirm_passphrase = self.confirm_passphrase_input.text()
            
            if passphrase != confirm_passphrase:
                QMessageBox.warning(self, "Erreur", "Les passphrases ne correspondent pas!")
                return
            
            key_path = Path(self.path_input.text())
            
            # Vérifier si le fichier existe déjà
            if key_path.exists():
                reply = QMessageBox.question(
                    self,
                    "Fichier existant",
                    f"Le fichier {key_path} existe déjà. Voulez-vous le remplacer?",
                    QMessageBox.Yes | QMessageBox.No
                )
                if reply == QMessageBox.No:
                    return
            
            # Créer le répertoire .ssh si nécessaire
            key_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Générer la clé selon le type choisi
            key_type = self.key_type_combo.currentText()
            comment = self.email_input.text().encode('utf-8') if self.email_input.text() else b""
            
            if "Ed25519" in key_type:
                private_key = ed25519.Ed25519PrivateKey.generate()
                public_key = private_key.public_key()
            else:
                key_size = self.key_size_spin.value()
                private_key = rsa.generate_private_key(
                    public_exponent=65537,
                    key_size=key_size,
                    backend=default_backend()
                )
                public_key = private_key.public_key()
            
            # Déterminer l'encryption pour la clé privée
            if passphrase:
                encryption_algorithm = serialization.BestAvailableEncryption(passphrase.encode('utf-8'))
            else:
                encryption_algorithm = serialization.NoEncryption()
            
            # Sérialiser la clé privée
            private_pem = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.OpenSSH,
                encryption_algorithm=encryption_algorithm
            )
            
            # Sérialiser la clé publique
            public_openssh = public_key.public_bytes(
                encoding=serialization.Encoding.OpenSSH,
                format=serialization.PublicFormat.OpenSSH
            )
            
            # Ajouter le commentaire à la clé publique
            if comment:
                public_openssh = public_openssh + b" " + comment
            
            # Sauvegarder les clés
            with open(key_path, 'wb') as f:
                f.write(private_pem)
            os.chmod(key_path, 0o600)
            
            public_key_path = key_path.with_suffix(key_path.suffix + '.pub')
            with open(public_key_path, 'wb') as f:
                f.write(public_openssh)
            os.chmod(public_key_path, 0o644)
            
            # Stocker pour copie ultérieure
            self.generated_public_key = public_openssh.decode('utf-8')
            self.generated_key_path = key_path
            
            # Afficher le résultat
            result_message = f"""✅ Clés SSH générées avec succès!

Type: {key_type}
Clé privée: {key_path}
Clé publique: {public_key_path}

Permissions:
- Clé privée: 600 (lecture/écriture propriétaire uniquement)
- Clé publique: 644 (lecture pour tous)

Clé publique:
{self.generated_public_key}

📋 Vous pouvez copier la clé publique avec le bouton ci-dessous.

💡 Pour utiliser cette clé:
1. Copiez la clé publique sur votre serveur
2. Ajoutez-la à ~/.ssh/authorized_keys
   ou utilisez: ssh-copy-id -i {public_key_path} user@host
"""
            self.result_text.setPlainText(result_message)
            
            QMessageBox.information(
                self,
                "Succès",
                f"Clés SSH générées avec succès!\n\nClé privée: {key_path}\nClé publique: {public_key_path}"
            )
            
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Erreur lors de la génération de la clé:\n{str(e)}")
            self.result_text.setPlainText(f"❌ Erreur: {str(e)}")
    
    def copy_public_key(self):
        """Copie la clé publique dans le presse-papier"""
        if self.generated_public_key:
            clipboard = QApplication.clipboard()
            clipboard.setText(self.generated_public_key)
            QMessageBox.information(self, "Copié", "La clé publique a été copiée dans le presse-papier!")
        else:
            QMessageBox.warning(self, "Attention", "Aucune clé générée à copier.")
    
    def open_folder(self):
        """Ouvre le dossier contenant les clés"""
        if self.generated_key_path:
            folder_path = self.generated_key_path.parent
            try:
                subprocess.run(['xdg-open', str(folder_path)], check=True)
            except Exception as e:
                QMessageBox.warning(self, "Erreur", f"Impossible d'ouvrir le dossier:\n{str(e)}")
        else:
            QMessageBox.warning(self, "Attention", "Aucune clé générée.")


def main():
    app = QApplication(sys.argv)
    window = SSHKeyGenerator()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
