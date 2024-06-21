def stat(data: list[float]) -> dict:
    min_temp = min(data)
    max_temp = max(data)
    mean_temp = sum(data) / len(data)
    median_temp = calculate_median(data)

    return {
        'min': min_temp,
        'max': max_temp,
        'mean': mean_temp,
        'median': median_temp
    }


def calculate_median(data: list[float]) -> float:
    data.sort()

    n = len(data)
    mid = n // 2

    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]
