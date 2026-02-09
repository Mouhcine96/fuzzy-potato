# App Stack (nginx + python app + postgres)

## Start
cd ~/fuzzy-potato/docker/app-stack
docker compose up -d

## Status
docker compose ps
curl -i http://localhost:8081

## Logs
docker compose logs --tail=100 web
docker compose logs --tail=100 app
docker compose logs --tail=100 db

## Stop
docker compose down

## Troubleshooting
- Config prüfen: docker compose config
- Health: docker inspect --format='{{json .State.Health}}' app | jq
- Nginx upstream: docker exec -it web nginx -T
1~# App Stack (nginx + python app + postgres)

## Start
cd ~/fuzzy-potato/docker/app-stack
docker compose up -d

## Status
docker compose ps
curl -i http://localhost:8081

## Logs
docker compose logs --tail=100 web
docker compose logs --tail=100 app
docker compose logs --tail=100 db

## Stop
docker compose down

## Troubleshooting
- Config prüfen: docker compose config
- Health: docker inspect --format='{{json .State.Health}}' app | jq
- Nginx upstream: docker exec -it web nginx -T
