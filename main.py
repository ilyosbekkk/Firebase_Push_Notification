import time

import requests
import json
from oauth2client.service_account import ServiceAccountCredentials
import schedule
import threading

hours1 = ['00:00', '00:00', '00:00', '00:00']
hours2 = ['00:00', '00:00', '00:00', '00:00']

PROJECT_ID = 'moca-7c36d'
SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']
BASE_URL = 'https://fcm.googleapis.com'
FCM_ENDPOINT = 'v1/projects/' + PROJECT_ID + '/messages:send'
FCM_URL = BASE_URL + '/' + FCM_ENDPOINT


def _get_access_token():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'service-account.json', SCOPES)
    access_token_info = credentials.get_access_token()

    return access_token_info.access_token


def _send_fcm_message(fcm_message):
    headers = {
        'Authorization': 'Bearer ' + _get_access_token(),
        'Content-Type': 'application/json; UTF-8',
    }

    resp = requests.post(FCM_URL, data=json.dumps(fcm_message), headers=headers)

    if resp.status_code == 200:
        print('Message sent to Firebase for delivery, response:')
        print(resp.text)
    else:
        print('Unable to send message to Firebase')
        print(resp.text)


def _build_common_message(topic):
    return {
        'message': {
            'topic': topic,
            'notification': {
                'title': 'FCM Notification',
                'body': 'Notification from FCM'
            },

        },

    }


def schdeule_notification(topic, hours):
    schedule.every().days.at(hours[0]).do(_send_fcm_message, _build_common_message(topic))
    schedule.every().days.at(hours[1]).do(_send_fcm_message, _build_common_message(topic))
    schedule.every().days.at(hours[2]).do(_send_fcm_message, _build_common_message(topic))
    schedule.every().days.at(hours[3]).do(_send_fcm_message, _build_common_message(topic))

    while 1:
        schedule.run_pending()
        time.sleep(1)


threading.Thread(target=schdeule_notification, args=("time1", hours1)).start()
threading.Thread(target=schdeule_notification, args=("time2", hours2)).start()
