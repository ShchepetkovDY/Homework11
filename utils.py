import json


def load_candidates_from_json():
    """
    Функция чтения из файла
    Args: -
    Returns: список с кандидатами
    """

    with open("candidates.json", "rt", encoding="utf-8") as file:
        candidates = json.load(file)
        return candidates


def get_all():
    """
    Функция, которая выводит всех кандидатов
    """
    return load_candidates_from_json()


def get_candidate(candidate_id):
    """
    Функция, которая возвращает одного кандидата по его id
    Args: candidate_id
    Returns: Кандидат в зависимости от id
    """
    candidates = get_all()
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """
    Функция, которая возвращает кандидатов по имени
    Args: candidate_name
    Returns: список кандидатов в зависимости от candidate_name
    """
    candidates = get_all()
    result = []
    for candidate in candidates:
        if candidate["name"] == candidate_name:
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name):
    """
    Функция, которая возвращает кандидатов по навыку
    Args: skill_name
    Returns: список кандидатов в зависимости от skill_name
    """
    candidates = get_all()
    result = []
    for candidate in candidates:
        if skill_name in candidate["skills"].lower().split(", "):
            result.append(candidate)
    return result
