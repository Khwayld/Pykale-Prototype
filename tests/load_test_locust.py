from locust import HttpUser, task

class StreamlitUser(HttpUser):
    @task
    def load_homepage(self):
        self.client.get("/")