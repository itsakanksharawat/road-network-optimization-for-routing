def validate_paths(raw_result, clean_result):
    raw_length = raw_result["length"]
    clean_length = clean_result["length"]

    if raw_length == 0:
        return {"error": "Invalid raw path length"}

    diff = abs(raw_length - clean_length)
    percent = (diff / raw_length) * 100

    return {
        "length_difference": diff,
        "percentage_difference": percent
    }