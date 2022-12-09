from model.project import Project

def test_add_project(app):
    old_projects = app.mantis.get_project_list()
    project = Project(name="testname14", description="testdescription", status='"30"', viewstate='"10"')
    app.mantis.add_project(project)
    new_projects = app.mantis.get_project_list()
    n = len(old_projects)
    m = 0
    for i in range(n):
        if old_projects[i].name == project.name:
            m += 1
    if m == 1:
        assert len(old_projects) == len(new_projects)
    else:
        assert len(old_projects) + 1 == len(new_projects)
