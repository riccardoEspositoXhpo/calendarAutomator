import globals
import utils
from google_apis import convert_to_RFC_datetime
from auth import auth_service


def create_recurring_event(calendar_name, start, end, title, desc, rrule):
    
    service = auth_service()
    event_body = utils.create_event_body(start = start, end = end, summary = title, description = desc, rrule = rrule)

    calendar_id = utils.get_calendar_id(calendar_name)

    response = service.events().insert(
        calendarId = calendar_id,
        body = event_body
    ).execute()

    print(response)


if __name__ == '__main__':

    MODE = None
    
    # MODE = globals.DELETE
    # MODE = globals.CREATE

    cal_name = globals.CAL_NAME

    if MODE == globals.CREATE:
        start_time = convert_to_RFC_datetime(2022, 5, 26, 13, 0)
        end_time = convert_to_RFC_datetime(2022, 5, 26, 14, 0)
        title = 'Testing New Recurring Event'
        description = 'I like to use programs to automate my life ok?'
        
        rrule = utils.create_rrule(frequency='DAILY', count = 4)

        create_recurring_event(cal_name, start_time, end_time, title, description, rrule)
    
    elif MODE == globals.DELETE:
        
        event_name = 'Testing New Recurring Event'
        utils.delete_event(cal_name, event_name)

    else:
        pass