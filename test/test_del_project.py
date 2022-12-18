from random import randrange

def test_del_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    index = randrange(len(app.mantis.get_project_list()))
    old_projects = app.soap.get_project_list(username, password)
    app.mantis.delete_project(index)
    new_projects = app.soap.get_project_list(username, password)
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(old_projects[index])
    assert sorted(old_projects, key=old_projects.name) == sorted(new_projects, key=new_projects.name)

