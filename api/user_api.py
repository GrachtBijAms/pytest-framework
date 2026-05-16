from core.api_client import BaseAPIClient

class UserAPI(BaseAPIClient):
    
    BASE_ENDPOINT = "/users"
    
    def __init__(self, base_url: str):
        super().__init__(base_url)

    def get_all_users(self):
        # GET /users
        return self.get(self.BASE_ENDPOINT)
        
    def get_user(self, user_id: int):
        # GET /users/{user_id}
        return self.get(f"{self.BASE_ENDPOINT}/{user_id}")

    def create_user(self, payload: dict):
        # POST /users
        return self.post(self.BASE_ENDPOINT, payload=payload)

    def update_user(self, user_id: int, payload: dict):
        # PUT /users/{user_id}
        return self.put(f"{self.BASE_ENDPOINT}/{user_id}", payload=payload)

    def delete_user(self, user_id: int):
        # DELETE /users/{user_id}
        return self.delete(f"{self.BASE_ENDPOINT}/{user_id}")