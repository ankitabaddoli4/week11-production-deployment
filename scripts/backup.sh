#!/bin/bash
echo "📦 Backing up database..."

docker exec -t postgres pg_dump -U user mydb > backup.sql