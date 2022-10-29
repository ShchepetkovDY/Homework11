from flask import Flask, render_template
from utils import get_all, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def page_main():
    """
    Представление главной страницы
    """
    candidates = get_all()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:id>")
def page_candidate(id):
    """
    Представление страницы кандидатов
    """
    candidate = get_candidate(id)
    if not candidate:
        return "Кандидат не найден"
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def page_search_candidate(candidate_name):
    """
    Представление поиска кандидатов по имени
    """
    candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates)


@app.route("/skill/<skill_name>")
def page_search_skill(skill_name):
    """
    Представление поиска кандидатов по скиллу
    """
    candidates = get_candidates_by_skill(skill_name)
    return render_template("skill.html", skill=skill_name, candidates=candidates)


app.run()
