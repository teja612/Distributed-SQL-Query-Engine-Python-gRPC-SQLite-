def optimize(ast: dict) -> dict:
    if "JOIN" in ast["type"]:
        return {"strategy": "hash_join", "cost": 42}
    return {"strategy": "full_scan", "cost": 100}
