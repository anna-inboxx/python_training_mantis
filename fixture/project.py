from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()

    def open_manage_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage Projects").click()


    def set_project_name(self, name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(name).click()
            wd.find_element_by_name(name).clear()
            wd.find_element_by_name(name).send_keys(text)

    def create_project(self, project):
        wd = self.app.wd
        self.open_manage_page()
        self.open_manage_project_page()
        #open create page
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        #set value_name
        self.set_project_name("name",project.name)
        #submit
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        # return to project page
        wd.find_element_by_link_text("Proceed").click()


    def select_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_link_text("%s" % name).click()


    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_manage_page()
        self.open_manage_project_page()
        self.select_project_by_name(name)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.open_manage_page()
        self.open_manage_project_page()
        self.project_cache = None

    project_cache = None

    def get_project_list(self):
        wd = self.app.wd
        self.open_manage_page()
        self.open_manage_project_page()
        self.project_cache = []
        rows = wd.find_elements_by_xpath("//table[@class='width100']//tr[@class='row-1' or @class='row-2']")
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            name = cells[0].text
            status = cells[1].text
            description = cells[4].text
            self.project_cache.append(Project(name=name, status=status, description=description))
        return list(self.project_cache)


    def count(self):
        wd = self.app.wd
        self.open_manage_page()
        self.open_manage_project_page()
        return len(wd.find_elements_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=')]"))

