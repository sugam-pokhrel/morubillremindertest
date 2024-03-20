
import requests
def login():
        url = 'https://api.moru.com.np/login'

        headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3MDY4NTAyMDYsIm5iZiI6MTcwNjg1MDIwNiwianRpIjoiOGZjNzM1YzEtMzljMy00Y2VmLWE0MjEtOTU2MTViYjE0MjY4IiwiZXhwIjoxNzA2OTM2NjA2LCJzdWIiOnsicGhvbmUiOiI5ODI0MDE2MzYyIiwiYXZhdGFyIjoiU1AiLCJuYW1lIjoiU3VnYW0gUG9raHJlbCIsInNlY3VyaXR5X2NvZGUiOiIwIn0sImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.3yNKwBGtkvDGZWVylN2oLd2VYZ3mdgn94J7yGDcY2Hfqw0WfEIUmU8XjCerhjNC45Mw7IZvenu4QrkrWinUicw',
            'Content-Type': 'application/json'
        }

        data={
"username": "9824016362",
"email":"sugamf7@gmail.com",
"password":"@Safal12345",
"otp":"72626",
"customer_id":"398",
"office_code":"352",
"sc_no":"012.06.014"



}       
        
        response = requests.post(url, headers=headers, json=data)
        json_data = response.json()
        print(json_data)
     


        return "Bearer "+json_data['data']['access_token']


login()


