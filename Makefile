default: help

help:
	@echo 'Comandos disponiveis:'
	@echo ''
	@echo 'Uso geral:'
	@echo ''
	@echo ' alias: 		Cria o alias de comando (evob) no ~/.bashrc'
	@echo ' build: 		Sobe os containers do projeto'
	@echo ' down:		Derruba os containers do projeto'
	@echo ' ps:			Lista os containers ativos do projeto'
	@echo ' docker-dev: faz o build do pojeto usando compose'
	


CURRENT_DIR = $(shell pwd)
PROJECT_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST)))/../)
APPS_DIR := "$(PROJECT_DIR)/apps"

ps:
	@docker compose ps -a

cur:
	@echo $(CURRENT_DIR)  $(PROJECT_DIR) 

docker-dev:
	docker compose -f "docker-compose-dev.yml" up -d --build
