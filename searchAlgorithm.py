from fuzzywuzzy import fuzz, process
# Если нужно быстрее: from rapidfuzz import fuzz, process

class SearchAlgorithm:
    def __init__(self, data: list[str]):
        """
        Инициализация поискового алгоритма.
        :param data: список строк для поиска
        """
        self.data = data

    def search(self, query: str, threshold: int = 65, limit: int = 5) -> list[tuple[str, int]]:
        """
        Выполняет нечеткий поиск по запросу.
        :param query: строка-запрос
        :param threshold: минимальный процент совпадения
        :param limit: максимальное количество результатов
        :return: список кортежей (совпавшая строка, процент совпадения)
        """
        results = process.extract(
            query,
            self.data,
            scorer=fuzz.token_sort_ratio,
            limit=limit
        )

        # Фильтруем по порогу threshold
        filtered = [(match, score) for match, score in results if score >= threshold]

        return filtered


if __name__ == "__main__":
    dataset = [
        "Python Developer",
        "Junior Python Engineer",
        "Data Scientist",
        "Machine Learning Engineer",
        "Backend Developer",
        "Frontend Engineer"
    ]

    searcher = SearchAlgorithm(dataset)

    query = "pyton devloper"  # намеренно с ошибкой
    matches = searcher.search(query, threshold=70, limit=5)

    print(f"Запрос: {query}")
    if matches:
        for match, score in matches:
            print(f"- {match} ({score}%)")
    else:
        print("❌ Ничего не найдено")
