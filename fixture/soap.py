from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        soap_project_list = []
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        result = client.service.mc_projects_get_user_accessible(username, password)
        for elem in result:
            name = elem['name']
            description = elem['description']
            status = elem['status']['name']
            viewstate = elem['view_state']['name']
            soap_project_list.append(Project(name=name, description=description, status=status, viewstate=viewstate))
        return soap_project_list


