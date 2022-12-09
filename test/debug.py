def debug(app):
    project_list = app.mantis.get_project_list()
    print(project_list)
