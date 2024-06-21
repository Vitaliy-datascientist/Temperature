def get_data(path: str) -> list[str]:
    with open(path, 'r', encoding='utf-8') as file:
        return file.readlines()


def clean_data(data: list[str]) -> list[float]:
    return [float(num.strip()) for num in data if num.strip()]
