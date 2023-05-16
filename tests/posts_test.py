import utils
import pytest
import pprint
import sys

pprint.pprint(sys.path)



def test_get_all_type():

    posts = utils.get_posts_all()
    assert type(posts) == list, "Не получается список комменатриев"
    assert len(posts) == 8

def test_get_all_check_structure():

    posts = utils.get_posts_all()
    first_post = posts[0]
    keys_expected = {"poster_name","poster_avatar", "pic", "content","views_count","likes_count","pk"}
    first_post_keys = set(first_post.keys())
    assert first_post_keys == keys_expected, "Полученные ключи неверны"

parameters_get_by_pk = [1,2,3,4]
@pytest.mark.parametrize("post_pk", parameters_get_by_pk)
def test_get_by_pk_check_format_and_keys(utils,post_pk):

    post = utils.get_post_by_pk(post_pk)


def test_get_by_pk_check_not_exist(utils):
    no_post = utils.get_post_by_pk(0)
    assert no_post == None













