import json
import re

#1. Возвращает все посты.

def get_posts_all():

    with open(r"C:\Users\Aleksei\PycharmProjects\Kursovaia_1\static\data\posts.json","r",encoding = "utf-8") as file:
        data = json.load(file)
        return data

#2. Возвращает комментарии, относящиеся к посту

def get_comments_by_post_id(post_id):

    comments_by_post_id = []

    with open(r"C:\Users\Aleksei\PycharmProjects\Kursovaia_1\static\data\comments.json","r",encoding = "utf-8") as file:
        data = json.load(file)
        for index in range(len(data)):
            if data[index]["post_id"] == post_id:

                comments_by_post_id.append(data[index])

        return comments_by_post_id # возвращает список словарей с нужными комментариями

#3. Получить пост по идентификатору

def get_post_by_pk(pk):

    with open(r"C:\Users\Aleksei\PycharmProjects\Kursovaia_1\static\data\posts.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        for index in range(len(data)):
            if data[index]["pk"] == pk:
                return data[index]


def search_by_name_or_content(search_request):

    search_result = []
    lower_search_request = search_request.lower()

    with open(r"C:\Users\Aleksei\PycharmProjects\Kursovaia_1\static\data\posts.json","r",encoding = "utf-8") as file:
        data = json.load(file)
        for index in range(len(data)):
            if data[index]["poster_name"] == lower_search_request:
                search_result.append(data[index])

            else:

                for value in data[index].values():
                    if search_request in str(value).lower():
                        search_result.append(data[index])

        return search_result



def add_to_bookmarks(pk):

    try:

        with open("./static/data/bookmarks.json", "r+") as file1:
            data_bookmarks = json.load(file1)

        if len(data_bookmarks) == 0:

            with open("./static/data/posts.json", "r", encoding="utf-8") as file2:
                data_posts = json.load(file2)

            for index2 in range(len(data_posts)):

                if pk in data_posts[index2].values():

                    data_bookmarks.append(data_posts[index2])

                    break


            with open("./static/data/bookmarks.json", "w", encoding="utf-8") as file1:
                json.dump(data_bookmarks, file1, ensure_ascii="False")

            return data_posts

        else:

            for index1 in range(len(data_bookmarks)):

                with open("./static/data/posts.json", "r", encoding = "utf-8") as file2:
                    data_posts = json.load(file2)

                for index2 in range(len(data_posts)):

                    if data_posts[index2]["pk"] == pk:

                        data_bookmarks.append(data_posts[index2])

                        temp =[]

                        for x in data_bookmarks:
                            if x not in temp:
                                temp.append(x)

                        data_bookmarks = temp

                    with open("./static/data/bookmarks.json", "w", encoding = "utf-8") as file1:
                        json.dump(data_bookmarks, file1, ensure_ascii = "False")

        return data_bookmarks

    except FileNotFoundError:

        data_bookmarks = []

        with open("./static/data/posts.json", "r",
                  encoding = "utf-8") as file2:

            data_posts = json.load(file2)

            for index in range(len(data_posts)):
                if data_posts[index]["pk"] == pk:
                    data_bookmarks.append(data_posts[index])

            with open("./static/data/bookmarks.json", "w", encoding = "utf-8") as file1:
                json.dump(data_bookmarks, file1, ensure_ascii = "False")

            return data_bookmarks


##################################################################################################################

def get_bookmarks():

    try:

        with open("./static/data/bookmarks.json", "r") as file:
            data_bookmarks = json.load(file)

    except FileNotFoundError:

        data_bookmarks = []

    return data_bookmarks




##################################################################################################################

def remove_bookmark(pk):

    with open("./static/data/bookmarks.json", "r", encoding = "utf-8") as file1:
        data_bookmarks = json.load(file1)

    for index1 in range(len(data_bookmarks)):

        if pk in data_bookmarks[index1].values():

            del data_bookmarks[index1]

            break

    with open("./static/data/bookmarks.json", "w", encoding="utf-8") as file1:
        json.dump(data_bookmarks, file1, ensure_ascii="False")

def check_for_hashtag(post):

    tag = "#"

    if tag in post["content"]:

        divided_by_words = post["content"].split()

        for word in divided_by_words:

            if word[0] == "#":

                number = divided_by_words.index(word)

                updated_word = '<a href = "/tag/'+ word[1:]+'">'+ word +'</a>'

                divided_by_words[number] = updated_word

        updated_content = ' '.join(divided_by_words)

        post.update({"content":updated_content})

        return post

    else:

        return post






# def tag_task():
#
#     tag = "#"
#
#     with open("./static/data/posts.json", "r",
#               encoding = "utf-8") as file:
#
#         data_posts = json.load(file)
#
#         for item in data_posts:
#
#             if tag in item["content"]:
#
#                 print(item["content"])
#
#                 count = 0
#
#                 for ch in item["content"]:
#
#                     count += 1
#                     start = []
#
#                     if ch == tag:
#
#                         start.append(count)
#
#                         print(start)
#
#
#
# tag_task()









# def search_for_posts(query):
#
#     lower_query = query.lower()
#
#     search_result = []
#
#     with open("./static/data/posts.json","r",encoding = "utf-8") as file:
#         data = json.load(file)
#         for index in range(len(data)):
#             for value in data[index].values():
#                 if query in str(value).lower():
#                     search_result.append(data[index])
#     return search_result



# def get_posts_by_user(user_name):
#
#     try:
#
#         posts_by_user = []
#
#         with open("./static/data/posts.json","r",encoding = "utf-8") as file:
#             data = json.load(file)
#             for index in range(len(data)):
#                 if data[index]["poster_name"] == user_name:
#                     posts_by_user.append(data[index])
#
#             return posts_by_user # возвращает список словарей от нужного пользователя
#
#     except ValueError:
#
#         print('У пользователя нет постов или пользователя с таким именем нет')









# with open("./static/data/bookmarks.json", "r",
#           encoding="utf-8") as file1:
#     data_bookmarks = json.load(file1)
#
#     for index1 in range(len(data_bookmarks)):
#
#         if data_bookmarks[index1]["pk"] == pk:
#
#             print(f'Да это уже было ..')  # Если номер такого поста уже был то цикл завершается
#
#         else:
#
#             with open("./static/data/posts.json", "r",
#                       encoding="utf-8") as file2:
#
#                 data_posts = json.load(file2)
#
#             for index2 in range(len(data_posts)):
#
#                 if data_posts[index2]["pk"] == pk:
#                     data_bookmarks.append(data_posts[index2])
#
#                     with open("./static/data/bookmarks.json", "w+",
#                               encoding="utf-8") as file1:
#                         json.dump(data_bookmarks, file1, ensure_ascii="False")















