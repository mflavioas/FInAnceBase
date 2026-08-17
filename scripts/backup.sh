#!/bin/bash
# FinKnowledge Backup Script
# Performs a pg_dump of the PostgreSQL database and backs up Qdrant snapshots.

set -e

BACKUP_DIR="/data/backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

echo "Starting backup process..."

# 1. PostgreSQL Backup
echo "Dumping PostgreSQL database 'finknowledge'..."
# Uses env vars: PGPASSWORD, PGUSER, PGHOST
pg_dump -U postgres -h localhost finknowledge > "$BACKUP_DIR/finknowledge_pg.sql"

# 2. Qdrant Backup (Vector DB)
# Qdrant supports creating snapshots via API
echo "Creating Qdrant snapshot..."
curl -s -X POST "http://localhost:6333/collections/finknowledge_vectors/snapshots" > "$BACKUP_DIR/qdrant_snapshot_info.json"

echo "Backup completed successfully at $BACKUP_DIR"
