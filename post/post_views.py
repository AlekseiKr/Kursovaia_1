from flask import Blueprint,render_template
import utils

post_blueprint = Blueprint("post_blueprint",__name__)

@post_blueprint.route('/posts/<int:pk>')
def page_post(pk):

    post = utils.get_post_by_pk(pk)

    check_for_hashtag = utils.check_for_hashtag(post)

    print(check_for_hashtag)

    data = utils.get_posts_all()

    post_id = pk
    comments = utils.get_comments_by_post_id(post_id)

    bookmarks = utils.get_bookmarks()

    if len(bookmarks) == 0:
        bookmarks = None

    else:
        bookmarks = bookmarks


    return render_template ('post.html', data = check_for_hashtag, bookmarks = bookmarks, comments = comments, views_count = data[pk-1]["views_count"])