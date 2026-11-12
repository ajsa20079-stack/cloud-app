# cloud-app — Автосалон (Казахстан)

Flask-приложение, CI/CD на GitHub Actions: Checkout → Install → Test → Docker build → Push (GHCR) → Deploy (SSH).

## Запуск локально
    pip install -r requirements.txt
    pytest
    python app.py        # http://localhost:5000

## Секреты репозитория (Settings → Secrets → Actions)
- SERVER_HOST — IP сервера (VPS с установленным Docker)
- SERVER_USER — пользователь SSH
- SERVER_SSH_KEY — приватный SSH-ключ
- GHCR_TOKEN — Personal Access Token с правом read:packages
