FROM debian:latest
RUN set -x \
&& apt update -y \
&& apt install nano -y \
&& apt install apache2 -y \
&& apt install ssh -y \
&& apt install mariadb-server -y \
&& apt install php -y

#1FROMImage parente
#2MAINTAINERAuteur
#3ARGVariables passées comme paramètres à la construction de l'image
#4ENVVariable d'environnement
#4LABELAjout de métadonnées
#5VOLUMECrée un point de montage
#6RUNCommande(s) utilisée(s) pour construire l'image
#6COPYAjoute un fichier dans l'image
#6WORKDIRPermet de changer le chemin courant
#7EXPOSEPort(s) écouté(s) par le conteneur
#8USERNom d'utilisateur ou UID à utiliser
#9ONBUILDInstructions exécutées lors de la construction d'images enfants
#10CMDExécuter une commande au démarrage du conteneur
#10ENTRYPOINTExécuter une commande au démarrage du conteneur