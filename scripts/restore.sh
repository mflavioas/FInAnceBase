#!/bin/bash
# FinKnowledge Restore Script
# Restores a pg_dump to PostgreSQL. Qdrant restores must be done via API with the snapshot file.

set -e

if [ -z "$1" ]; then
  echo "Usage: $0 <path_to_sql_dump>"
  exit 1
fi

DUMP_FILE="$1"

if [ ! -f "$DUMP_FILE" ]; then
  echo "Error: File $DUMP_FILE not found!"
  exit 1
fi

echo "Restoring PostgreSQL database 'finknowledge' from $DUMP_FILE..."
psql -U postgres -h localhost -d finknowledge -f "$DUMP_FILE"

echo "Restore of PostgreSQL completed."
echo "For Qdrant, please upload the snapshot via their API: PUT /collections/finknowledge_vectors/snapshots/recover"
