from random import randrange

def test_del_project(app):
    index = randrange(len(app.mantis.get_project_list()))
    old_projects = app.soap.get_project_list(app)
    app.mantis.delete_project(index)
    new_projects = app.soap.get_project_list(app)
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(old_projects[index])
    assert sorted(old_projects, key=lambda x: x.name) == sorted(new_projects, key=lambda x: x.name)

