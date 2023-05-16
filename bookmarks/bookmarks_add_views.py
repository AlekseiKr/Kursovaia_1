from flask import Blueprint,render_template, redirect
import utils

bookmarks_blueprint = Blueprint("bookmarks_blueprint",__name__)

@bookmarks_blueprint.route('/bookmarks/add/<int:pk>')
def bookmark_add(pk):

    bookmarks = utils.add_to_bookmarks(pk)

    return redirect("/", code = 302)