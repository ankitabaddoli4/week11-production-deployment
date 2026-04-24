#!/bin/bash
echo "🚀 Deploying app..."
docker-compose -f docker/docker-compose.prod.yml up -d --build
