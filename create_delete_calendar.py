from google_apis import create_service
from auth import auth_service
import utils
import globals

def create_calendar(cal_name):

    request_body = {
        'summary':  cal_name
    }

    service = auth_service()
    response = service.calendars().insert(body=request_body).execute()
    print(response)

    # save response to filesystem in json format
    utils.save_response(globals.WORKING_DIR, globals.JSON_DIR, cal_name, response)



def delete_calendar(cal_name):


    calendar_id = utils.get_calendar_id(cal_name)

    service = auth_service()
    response = service.calendars().delete(calendarId=calendar_id).execute()
    print(response)


def create_delete_helper(mode, cal_name):

    return delete_calendar(cal_name) if mode == "delete" else create_calendar(cal_name)


if __name__ == '__main__':

    MODE = None
    CAL_NAME = globals.CAL_NAME

    if MODE == globals.CREATE or MODE == globals.DELETE:
        create_delete_helper(MODE, CAL_NAME)

    else:
        pass