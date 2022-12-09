from random import randrange

def test_del_project(app):
    index = randrange(len(app.mantis.get_project_list()))
    app.mantis.delete_project(index)