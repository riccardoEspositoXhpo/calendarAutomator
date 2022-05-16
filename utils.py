from xml.dom.expatbuilder import parseString
import globals
import json
import os
from auth import auth_service
from dateutil.rrule import rrulestr



def get_calendar_id_offline(cal_name):

    # loop directory to find calendar
    for filename in os.listdir(globals.JSON_DIR):
        
        if filename == cal_name + '.json':
            
            # load calendar data and grab id        
            json_file = open(globals.JSON_DIR + '/' + filename)
            calendar_metadata = json.load(json_file)
            calendar_id = calendar_metadata['id']
            return calendar_id

    raise FileNotFoundError


def get_calendar_id(cal_name):

    service = auth_service()

    page_token = None
    while True:
        
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        
        for calendar_list_entry in calendar_list['items']:
            
            if calendar_list_entry['summary'] == cal_name:
                return calendar_list_entry['id']
        
        page_token = calendar_list.get('nextPageToken')
        
        if not page_token:
            raise CalNotFoundException


def create_event_body(**params):

    body = {
        'start' : {
            'dateTime': params['start'],
            'timeZone': 'Europe/Zurich'
        },
        'end' : {
            'dateTime': params['end'],
            'timeZone': 'Europe/Zurich'
        }
    }

    try:
        body['summary'] = params['summary']
    
    except KeyError:
        pass

    try:
        body['description'] = params['description']
    
    except KeyError:
        pass
    
    try:
        body['recurrence'] = [params['rrule']]

    except KeyError:
        pass    

    return body




    
def save_response(current_dir, subdir, cal_name, response):
    if not os.path.exists(os.path.join(current_dir, subdir)):
        os.mkdir(os.path.join(current_dir, subdir))

    with open(subdir + '/' + cal_name + ".json", 'w') as out_file:
        json.dump(response, out_file)


def create_rrule(**params):

    delimiter = ';'
    # grab rrule parameters
    frequency = params.get('frequency', False)
    count = params.get('count', False)
    # NOT SUPPORTED
    # until = params.get('until', False)
    on_days = params.get('on_days', False)
    interval = params.get('interval', False)

    assert frequency, "Frequency is required"
    
    rrule = 'RRULE:FREQ=' + frequency + delimiter

    if count:
        rrule += "COUNT=" + str(count) + delimiter

    if interval:
        rrule += "INTERVAL=" + str(interval) + delimiter

    if on_days:
        rrule += "BYDAY=" + on_days + delimiter

    if rrule[-1] == ';':
        rrule = rrule[:-1]

    if is_rrule_valid(frequency, count, interval, on_days):
        return rrule
    
    else:  
        raise InvalidRRuleException


def is_rrule_valid(frequency, count, interval, on_days):
    
    frequencies = [globals.DAILY, globals.WEEKLY, globals.MONTHLY]
    days = [globals.MONDAY, globals.TUESDAY, globals.WEDNESDAY, globals.THURSDAY, 
            globals.FRIDAY, globals.SATURDAY, globals.SUNDAY]

    assert frequency in frequencies, "Incorrect Frequency"
    assert isinstance(count, int), "Count must be an integer"
    
    if interval:
        assert isinstance(interval, int), "Interval must be an integer"
    
    if on_days:
        assert on_days in days, "Wrong Day(s) of the week"

    return True
    


def get_event_id(cal_id, event_name):

    service = auth_service()
    page_token = None

    while True:
    
        events = service.events().list(calendarId=cal_id, pageToken=page_token).execute()
    
        for event in events['items']:
            if event['summary'] == event_name:
                return event['id']

            page_token = events.get('nextPageToken')
    
        if not page_token:
            raise EventNotFoundException





def delete_event(cal_name, event_name):
    
    service = auth_service()
    cal_id = get_calendar_id(cal_name)
    event_id = get_event_id(cal_id, event_name)

    response = service.events().delete(calendarId=cal_id, eventId=event_id).execute()

    print(response)



class InvalidRRuleException(Exception):
    """Signals invalid Rrule"""
    pass

class CalNotFoundException(Exception):
    """Signals invalid Rrule"""
    pass

class EventNotFoundException(Exception):
    """Signals invalid Rrule"""
    pass



if __name__ == '__main__':

    pass
    