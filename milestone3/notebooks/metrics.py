# Define custom decorator to automatically calculate metric based on key
metrics = {}
metric = lambda f: metrics.setdefault(f.__name__, f)

@metric
def ap(results, relevant):
    """Average Precision"""
    precision_values = [
        len([
            doc 
            for doc in results[:idx]
            if doc['tconst'] in relevant
        ]) / idx 
        for idx in range(1, len(results))
    ]
    return sum(precision_values)/len(precision_values)

@metric
def p10(results, relevant, n=10):
    """Precision at N"""
    return len([doc for doc in results[:n] if doc['tconst'] in relevant])/n

@metric
def p15(results, relevant, n=15):
    """Precision at N"""
    return len([doc for doc in results[:n] if doc['tconst'] in relevant])/n

@metric
def ia(results, relevant, n=10):
    """Individual Assessment at N"""
    return "".join(["R" if doc['tconst'] in relevant else "N" for doc in results[:n]])

def calculate_metric(key, results, relevant):
    return metrics[key](results, relevant)
