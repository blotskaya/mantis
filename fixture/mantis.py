from model.project import Project

class MantisHelper:

    def __init__(self, app):
        self.app = app

    def open_main_page(self):
        wd = self.app.wd
        # open contacts page
        if not wd.current_url.endswith("/my_view_page.php"):
            self.app.open_home_page()

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def add_project(self, project):
        wd = self.app.wd
        self.open_main_page()
        self.open_projects_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.project_cache = None

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)
        wd.find_element_by_css_selector('select[name="status"] > option[value=%s]' % project.status).click()
        wd.find_element_by_css_selector('select[name="view_state"] > option[value=%s]' % project.viewstate).click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_main_page()
            self.open_projects_page()
            self.project_cache = []
            for row in wd.find_elements_by_xpath("//table[@class='width100']")[1].find_elements_by_css_selector(".row-1, .row-2"):
                cells = row.find_elements_by_tag_name("td")
                name = cells[0].text
                description = cells[4].text
                status = cells[1].text
                viewstate = cells[3].text
                self.project_cache.append(Project(name=name, status=status, viewstate=viewstate, description=description))
        return list(self.project_cache)

    def select_project_by_index(self, index):
        wd = self.app.wd
        # select contact
        wd.find_elements_by_xpath("//table[@class='width100']")[1].find_elements_by_css_selector("a[href *= 'manage_proj_edit_page']")[index].click()

    def delete_project(self, index):
        wd = self.app.wd
        self.open_main_page()
        self.open_projects_page()
        self.select_project_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None
