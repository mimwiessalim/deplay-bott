# Bot de Telegram

## Descripción
Bot simple de Telegram que responde "Hola mundo 👋" a cualquier mensaje de texto que reciba.

## Fecha de Creación
17 de octubre de 2025

## Tecnologías
- Python 3.11
- python-telegram-bot 13.15

## Configuración
El bot utiliza la variable de entorno TELEGRAM_BOT_TOKEN para autenticarse con la API de Telegram. Este token está configurado de forma segura en Replit Secrets.

## Estructura del Proyecto
- main.py: Código principal del bot
- pyproject.toml: Configuración de dependencias del proyecto

## Estado Actual
El bot está funcionando correctamente y esperando mensajes en Telegram.

## Cambios Recientes
- 17/10/2025: Creación inicial del bot
- Se corrigió problema de seguridad: token movido de código a variable de entorno
- Se resolvió conflicto de dependencias entre paquetes python-telegram-bot y telegram
