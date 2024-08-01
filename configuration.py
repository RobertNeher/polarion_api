class Configuration:
    def __init__(self) -> None:
        self.polarionHost = 'localhost/polarion'
        self.polarionAPIPrefix = 'rest/v1'
        self.schema = "http"
        self.apiToken = 'eyJraWQiOiJmOWMyMmE2Yy0wYTAyMDkwNi0yYTljZTZhOS0zNzVlMWZiNiIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJyTmVoZXIiLCJpZCI6IjA4ZTFmNTM3LWMwYTgwMTJjLTBkNDI0ZjA4LTJlMWQ2MDZjIiwiZXhwIjoxNzI3NjQ3MjAwLCJpYXQiOjE3MjI0MzA5MTF9.wNUFL5r5MKG6NZqkBv9NRReWEQn0obYWMKA4FANB0ijp8gHPa00heedvxDxXPwNM4IR4siWPguYbJW6T5uEZw_4atXohxVQsqu9XWwnXvB4J6eLVPNmNV3Xrg6pP9E1G6yMUE6IVxPGBFouqNd51u3zOGxQJ1Yks7YsYoddNcKSK0l8Q-qwwa6jZlOHam8FmAPQICfMSQ0JoYyHGZJWGITao3GMLB-RNWL5QOyKWXtSm5DWElNZUqUbdn-TF9FcRT7m6goes5WmfLcL5WyUHNx7fJ285NP99TW00RF7POFEAu1Ko8tQUPewdSvCCXb-eIcW6ZWSAwH6Ncc46xBr-1g'
        self.header = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {self.apiToken}"
        }
        self.dataFilter = {
            "fields[projects]": "@all",
            "fields[document_attachments]": "@all",
            "fields[document_comments]": "@all",
            "fields[document_parts]": "@all",
            "fields[enumerations]": "@all",
            "fields[globalroles]": "@all",
            "fields[icons]": "@all",
            "fields[jobs]": "@all",
            "fields[linkedworkitems]": "@all",
            "fields[externallylinkedworkitems]": "@all",
            "fields[linkedoslcresources]": "@all",
            "fields[pages]": "@all",
            "fields[page_attachments]": "@all",
            "fields[plans]": "@all",
            "fields[projectroles]": "@all",
            "fields[projects]": "@all",
            "fields[projecttemplates]": "@all",
            "fields[testparameters]": "@all",
            "fields[testparameter_definitions]": "@all",
            "fields[testrecords]": "@all",
            "fields[teststep_results]": "@all",
            "fields[testruns]": "@all",
            "fields[testrun_attachments]": "@all",
            "fields[teststepresult_attachments]": "@all",
            "fields[testrun_comments]": "@all",
            "fields[usergroups]": "@all",
            "fields[users]": "@all",
            "fields[workitems]": "@all",
            "fields[workitem_attachments]": "@all",
            "fields[workitem_approvals]": "@all",
            "fields[workitem_comments]": "@all",
            "fields[featureselections]": "@all",
            "fields[teststeps]": "@all",
            "fields[workrecords]": "@all",
            "fields[revisions]": "@all",
            "fields[testrecord_attachments]": "@all"
        }