import requests
import json

serverToken = 'your server key here'
deviceToken = 'device token here'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'key=' + 'AAAAYTNDQUk:APA91bHdMGiTHYAFNyF5xl6xW6ygbgRFMtYGsdW1JaGoNhqr8dO1IkN6sJDIuRC7EaEYCmrUDCdcnz0D5dIUd_chstl6yzvlKy-H68pkO9Z9G--9dZw137QRW3iypEw-akVqPrFKSTew',
}

body = {
    'notification': {'title': 'Sending push form python script',
                     'body': 'Hi Ilyosbek  How  are you , are you  fine what are you doing  here?'
                     },
    'to':
        "d8_9RveaQJaVdLnOMTqZ5M:APA91bE_CGDaqNUcvul7baYJWHr62-4p_C4tXUCWqq5ojYb_pyv0YIMjZHS_Gcq4hlVIEmUP98RIMQX_Kglj6jR1ggIuBSjS1_aFqxrAg84C2p4o0gRa_Lf0g9L_kW3BRSEmdh1v-UZS",
    'priority': 'high',
}
response = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))
print(response.status_code)

print(response.json())
