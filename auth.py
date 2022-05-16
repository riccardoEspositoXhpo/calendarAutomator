from google_apis import create_service


def auth_service():

    API_SECRET = 'client_secret.json'
    API_NAME = 'calendar'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    service = create_service(API_SECRET, API_NAME, API_VERSION, SCOPES)

    # print(dir(service)) 
    return service






