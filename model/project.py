import requests
import json

from configuration import Configuration
from utils import polarionRequest

class Project():
    def __init__(self) -> None:
        config = Configuration()
        self.projects = []

        response = polarionRequest(f"/projects")

        if response == None:
            print(f"Request at end point '/projects' failed: {response.status_code}")
            exit

        projects = json.loads(response.text)["data"]

        for project in projects:
            self.projects.append(project)


    def getDetails(self, projectID: str) -> map:
        for project in self.projects:
            if project["id"] == projectID:
                return project["attributes"]


if __name__ == "__main__":
    projects = Project()

    for project in projects.projects:
        print(f"{project['id']}: {project['attributes']['name']}")