from auth import auth_service
from globals import *
import utils, classes, single_event, recurring_event, google_apis
from datetime import date


"""

This script aims to automate the management of recurring life activities.
By setting the appropriate variables in the classes file, one is able to
automatically create calendar events with the desired title and cadence.


DOX - Recurring events documentation
https://datatracker.ietf.org/doc/html/rfc2445#section-4.8.5.4


"""

# authenticate into google calendar API
auth_service()

# create class instances
indoorPlants = classes.WaterIndoorPlants()
lechuza = classes.WaterLechuza()
towels = classes.WashTowels()
bedsheets = classes.WashBedSheets()
glassAndPlastic = classes.GlassAndPlastic()


# generate dates 
today = date.today()
hour = 13
minute = 0
event_duration = 1

start_time = google_apis.convert_to_RFC_datetime(today.year, today.month, today.day, hour, minute)
end_time = google_apis.convert_to_RFC_datetime(today.year, today.month, today.day, hour + event_duration, minute)

# dummy count variable to have sufficient number of events
count = 10;

# formulate request - 
def create_all_events(cal_name, task_list):

    for task in task_list:

        # rrule = utils.create_rrule(frequency = task.frequency, interval = task.interval, count = count, on_days = task.on_days)
        rrule = utils.create_rrule(frequency = task.frequency, count = count, interval = task.interval, on_days = task.on_days)

        print(rrule)

        recurring_event.create_recurring_event(cal_name, start_time, end_time, task.title, task.description, rrule)

        print(task.title)


# delete events 
def delete_all_events(cal_name):

    service = auth_service()
    page_token = None
    cal_id = utils.get_calendar_id(cal_name)

    while True:
    
        events = service.events().list(calendarId=cal_id, pageToken=page_token).execute()
    
        for event in events['items']:
            
            response = service.events().delete(calendarId=cal_id, eventId=event['id']).execute()
            print(response)
            
            # print(event)
            page_token = events.get('nextPageToken')
    
        if not page_token:
            break



if __name__ == '__main__':

    MODE = None
    
    # MODE = CREATE
    # MODE = DELETE

    cal_name = CAL_NAME

    if MODE == CREATE:
        
        task_list = [indoorPlants, lechuza, towels, bedsheets, glassAndPlastic]
        create_all_events(cal_name, task_list)


    elif MODE == DELETE:
        
        delete_all_events(cal_name)

    else:
        pass

