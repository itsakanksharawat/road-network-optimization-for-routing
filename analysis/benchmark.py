def compare_graphs(raw_graph, clean_graph, source, target, routing_func):
    raw_result = routing_func(raw_graph, source, target)
    clean_result = routing_func(clean_graph, source, target)

    comparison = {
        "raw_time": raw_result["time"],
        "clean_time": clean_result["time"],
        "time_improvement": raw_result["time"] / clean_result["time"] if clean_result["time"] > 0 else None,

        "raw_length": raw_result["length"],
        "clean_length": clean_result["length"],
        "length_difference": abs(raw_result["length"] - clean_result["length"])
    }

    return raw_result, clean_result, comparison