# Distributed-SQL-Query-Engine-Python-gRPC-SQLite-

How to Run the Project
1. Initialize SQLite Shards
bash
for i in {0..2}; do
  sqlite3 shard_$i.db "CREATE TABLE users (id INT, name TEXT);"
  sqlite3 shard_$i.db "INSERT INTO users VALUES ($i, 'User $i');"
done
2. Start Worker Nodes
python
python worker.py  # Runs gRPC server on port 50051
3. Execute a Query
python
result = hash_join(
    worker1.ExecuteQuery("SELECT * FROM users").rows,
    worker2.ExecuteQuery("SELECT * FROM orders").rows,
    "user_id", "user_id"
)
