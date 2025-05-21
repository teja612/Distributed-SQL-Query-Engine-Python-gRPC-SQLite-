import sqlparse

def parse(sql: str) -> dict:
    parsed = sqlparse.parse(sql)[0]
    return {
        "type": "SELECT",
        "columns": [str(t) for t in parsed.tokens if isinstance(t, sqlparse.sql.Identifier)],
        "table": str(parsed.get_real_name()),
    }
