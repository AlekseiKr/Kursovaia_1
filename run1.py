from flask import Flask

from main.main_views import main_blueprint
from post.post_views import post_blueprint
from search.search_views import search_blueprint
from bookmarks.bookmarks_add_views import bookmarks_blueprint
from bookmarks.bookmarks_remove_views import bookmarks_remove_blueprint
from search.tag_views import tag_blueprint


app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(bookmarks_remove_blueprint)
app.register_blueprint(tag_blueprint)



if __name__ == "__main__":
    app.run(debug = True)