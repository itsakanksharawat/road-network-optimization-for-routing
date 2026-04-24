def compare_routes(graph, source, target, routing_func):
    modes = ["distance", "time", "congestion", "multi"]

    results = {}

    for mode in modes:
        try:
            result = routing_func(graph, source, target, mode)
            results[mode] = result
        except Exception as e:
            results[mode] = {"error": str(e)}

    return results