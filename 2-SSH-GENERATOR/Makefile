.PHONY: help build run stop clean logs shell test

# Couleurs pour l'affichage
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
RESET  := $(shell tput -Txterm sgr0)

help: ## Affiche cette aide
	@echo "${GREEN}Commandes disponibles:${RESET}"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  ${YELLOW}%-15s${RESET} %s\n", $$1, $$2}'

build: ## Construire l'image Docker
	@echo "${GREEN}Construction de l'image Docker...${RESET}"
	docker compose build

run: ## Lancer l'application
	@echo "${GREEN}Lancement de l'application...${RESET}"
	@xhost +local:docker > /dev/null 2>&1 || true
	@mkdir -p generated-keys
	docker compose up
	@xhost -local:docker > /dev/null 2>&1 || true

run-bg: ## Lancer l'application en arrière-plan
	@echo "${GREEN}Lancement en arrière-plan...${RESET}"
	@xhost +local:docker > /dev/null 2>&1 || true
	@mkdir -p generated-keys
	docker compose up -d
	@echo "${YELLOW}Utilisez 'make logs' pour voir les logs${RESET}"

stop: ## Arrêter l'application
	@echo "${GREEN}Arrêt de l'application...${RESET}"
	docker compose down
	@xhost -local:docker > /dev/null 2>&1 || true

restart: stop run ## Redémarrer l'application

clean: ## Supprimer les conteneurs et volumes
	@echo "${GREEN}Nettoyage...${RESET}"
	docker compose down -v
	@xhost -local:docker > /dev/null 2>&1 || true

clean-all: clean ## Nettoyage complet (images, conteneurs, volumes)
	@echo "${GREEN}Nettoyage complet...${RESET}"
	docker system prune -af --volumes

logs: ## Afficher les logs
	docker compose logs -f

shell: ## Ouvrir un shell dans le conteneur
	docker compose run --rm ssh-key-generator bash

ps: ## Afficher les conteneurs en cours
	docker compose ps

rebuild: clean build ## Reconstruction complète
	@echo "${GREEN}Reconstruction terminée${RESET}"

install-local: ## Installation locale (sans Docker)
	@echo "${GREEN}Installation locale des dépendances...${RESET}"
	pip3 install --user -r requirements.txt
	chmod +x ssh_key_generator.py
	@echo "${GREEN}Installation terminée. Lancez avec: python3 ssh_key_generator.py${RESET}"

test-x11: ## Tester la connexion X11
	@echo "${GREEN}Test de la connexion X11...${RESET}"
	@xhost +local:docker
	@docker run --rm -e DISPLAY=${DISPLAY} -v /tmp/.X11-unix:/tmp/.X11-unix alpine:latest sh -c "apk add --no-cache xeyes && xeyes" || echo "${YELLOW}Erreur X11 détectée${RESET}"
	@xhost -local:docker

check: ## Vérifier les prérequis
	@echo "${GREEN}Vérification des prérequis...${RESET}"
	@command -v docker >/dev/null 2>&1 || { echo "${YELLOW}❌ Docker non installé${RESET}"; exit 1; }
	@docker compose version >/dev/null 2>&1 || docker-compose --version >/dev/null 2>&1 || { echo "${YELLOW}❌ Docker Compose non installé${RESET}"; exit 1; }
	@echo "${GREEN}✅ Tous les prérequis sont installés${RESET}"

version: ## Afficher les versions
	@echo "${GREEN}Versions:${RESET}"
	@echo "Docker: $$(docker --version)"
	@echo "Docker Compose: $$(docker compose version 2>/dev/null || docker-compose --version 2>/dev/null)"
	@echo "Python: $$(python3 --version)"
