import requests
import json

from configuration import Configuration

class Project():
    def __init__(self) -> None:
        self.config = Configuration()
        self.projects = []
        self.url = f"{self.config.schema}://{self.config.polarionHost}/{self.config.polarionAPIPrefix}/projects"
        self.response = requests.get(url=self.url,
                params=self.config.dataFilter,
                headers={
                    "accept": "application/json",
                    "content-type": "application/json",
                    "authorization": f"Bearer {self.config.apiToken}"
                }
        )

        if self.response.status_code != 200:
            print(f"Request '{self.url}' failed: {self.response.status_code}")
            exit
    
        projects = json.loads(self.response.text)["data"]

        for project in projects:
            self.projects.append(project)


    def getProjectDetails(self, projectID: str) -> map:
        for project in self.projects:
            if project["id"] == projectID:
                return project["attributes"]


if __name__ == "__main__":
    projects = Project()
    projects.getProjectDetails("elibrary")