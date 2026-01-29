from locust import HttpUser, task, between

class EventsUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def view_events(self):
        with self.client.get(
            "/events?user=locust_user",
            name="/events",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Status code: {response.status_code}")
            else:
                response.success()