from locust import task, tag, HttpUser


class ObjectsPerforming(HttpUser):
    object_id = None

    def on_start(self):
        response = self.client.post(
            '/objects',
            json={
                "name": "Apple MacBook Pro 16",
                "data":
                    {"year": 2019,
                     "price": 1849.99,
                     "CPU model": "Intel Core i9",
                     "Hard disk size": "1 TB"
                     }
            }
        )
        self.object_id = response.json['id']

    @tag('Get all objects')
    @task(1)
    def get_all_objects(self):
        self.client.get('/objects')

    @tag('Get one object')
    @task(8)
    def get_one_object(self):
        self.client.get(f'/objects/{self.object_id}')

    @tag('Patch the object')
    @task(8)
    def update_patch_object(self):
        self.client.patch(
            f'/objects/{self.object_id}',
            json={"name": "Apple MacBook Pro 16 (Updated Name)"}
        )
