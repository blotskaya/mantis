from model.project import Project

def test_add_project(app):
    project = Project(name="testname", description="testdescription", status='"30"', viewstate='"10"')
    app.mantis.add_project(project)
