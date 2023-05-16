from flask import Blueprint,render_template, request
import utils


search_blueprint = Blueprint("search_blueprint",__name__)

@search_blueprint.route('/search', methods = ['POST'])
def search_page():

    search_request = request.form.get("search_request")

    search_result = utils.search_by_name_or_content(search_request)

    bookmarks = utils.get_bookmarks()

    if len(bookmarks) == 0:
        bookmarks = None

    else:
        bookmarks = bookmarks

    return render_template("search.html", data = search_result, query = search_request, bookmarks = bookmarks)





