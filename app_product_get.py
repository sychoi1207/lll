from locust import HttpUser,TaskSet,task,between

class WebTasks(TaskSet):
	@task
	def index(self):
		self.client.get("/pui/v1/page?pageId=MOHOMETODAYDLV")
		

class MyLocust(HttpUser):
	tasks = [WebTasks]
	host = "http://apl-iapis.11st.co.kr:8765"
	min_wait = 1000
	max_wait = 2000