def hash_join(left, right, left_key, right_key):
    hash_table = {row[left_key]: row for row in left}
    return [{**left_row, **right_row} for right_row in right 
            if (left_row := hash_table.get(right_row[right_key]))]
