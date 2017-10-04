from model.project import Project
import time

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_project_list()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        time.sleep(3)
        wd.find_element_by_css_selector("input[value='Create New Project']")

    def open_project_list(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_fill_value("name", project.name)

    def change_fill_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    project_cash = None

    def get_project_list(self):
        wd = self.app.wd
        projects = []
        row_1 = wd.find_elements_by_class_name("row-1")
        row_2 = wd.find_elements_by_class_name("row-2")
        project_lines = row_1 + row_2
        for element in project_lines:
            cells = element.find_elements_by_tag_name("td")
            name = cells[0].text
            #id = cells[0].get_attribute("href").text[36:]
            projects.append(Project(name=name, id=id))
        return projects