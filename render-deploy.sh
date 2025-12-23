set -e

alembic stamp head
alembic upgrade head
uvicorn src.main:app --host 0.0.0.0 --port $PORT