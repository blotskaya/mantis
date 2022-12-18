from model.project import Project

def test_add_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    old_projects = app.soap.get_project_list(username, password)
    project = Project(name="testname15", description="testdescription", status='"30"', viewstate='"10"')
    app.mantis.add_project(project)
    new_projects = app.soap.get_project_list(username, password)
    n = len(old_projects)
    m = 0
    for i in range(n):
        if old_projects[i].name == project.name:
            m += 1
    if m == 1:
        assert len(old_projects) == len(new_projects)
    else:
        assert len(old_projects) + 1 == len(new_projects)
        old_projects.append(project)
        assert sorted(old_projects, key=old_projects.name) == sorted(new_projects, key=new_projects.name)

