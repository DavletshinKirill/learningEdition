from flask import render_template
from . import education
from ..model import Languages, TopicNames, Notes
from flask_login import login_required


@education.route("/main_page")
@login_required
def get_languages():
    languages = Languages.query.filter_by().all()
    return render_template("main_menu.html", languages=languages, title="Main")


@education.route("/main_page/<language>")
@login_required
def get_topic_names(language):
    language = Languages.query.filter_by(language=language).first()
    topic_names = TopicNames.query.filter_by(language=language.id).all()
    return render_template("main_menu.html", topic_names=topic_names, title=language.language, language=language.language)


@education.route("/main_page/<language>/<topic_name>")
@login_required
def get_notes(language, topic_name):
    topic_names = TopicNames.query.filter_by(topic_name=topic_name).first()
    notes = Notes.query.filter_by(topic_names=topic_names.id).all()
    return render_template("main_menu.html", notes=notes, title=topic_names.topic_name, language=language)


@education.route("/main_page/<language>/<topic_name>/<title>")
@login_required
def get_note(language, topic_name, title):
    note = Notes.query.filter_by(title=title).first()
    return render_template("note.html", title=note.title, tutorial=note.tutorial)
