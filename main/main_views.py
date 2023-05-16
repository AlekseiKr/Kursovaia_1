from flask import Blueprint,render_template
import utils

main_blueprint = Blueprint("main_blueprint",__name__)

@main_blueprint.route('/')
def page_index():

    posts = utils.get_posts_all()
    bookmarks = utils.get_bookmarks()

    if len(bookmarks) == 0:
        bookmarks = None

    else:
        bookmarks = bookmarks


    return render_template("index.html", data = posts, bookmarks = bookmarks)

