from flask import Blueprint,render_template, request
import utils


tag_blueprint = Blueprint("tag_blueprint",__name__)

@tag_blueprint.route('/tag/<string:tagname>', methods = ['GET'])
def tag_page(tagname):

    search_request = "#" + tagname

    search_result = utils.search_by_name_or_content(search_request)

    bookmarks = utils.get_bookmarks()

    if len(bookmarks) == 0:
        bookmarks = None

    else:
        bookmarks = bookmarks

    return render_template("tag.html", data = search_result, query = search_request, bookmarks = bookmarks)





