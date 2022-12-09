from model.project import Project

def test_debug(app):
    project = Project(name="testname", description="testdescription", status='"30"', viewstate='"10"')
    project_list = app.mantis.get_project_list()
    n = len(project_list)
    m = 0
    for i in range(n):
        if project_list[i].name == project.name:
            m += 1
    if m == 1:
        print('true')
    else:
        print('false')

