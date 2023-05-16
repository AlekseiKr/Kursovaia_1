from flask import Blueprint,render_template, redirect
import utils

bookmarks_remove_blueprint = Blueprint("bookmarks_remove_blueprint",__name__)

@bookmarks_remove_blueprint.route('/bookmarks/remove/<int:pk>')
def bookmark_remove(pk):

    utils.remove_bookmark(pk)

    return redirect("/", code = 302)