#Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.
#To do this, you’ll need to know when any team is having a meeting. In HiCal, a meeting is stored as tuples ↴ of integers
#(start_time, end_time). These integers represent the number of 30-minute blocks past 9:00am.
#Write a function merge_ranges() that takes a list of meeting time ranges and returns a list of condensed ranges.

meetings = [(1,2),(3,5),(4,6)]
#(start_time,end_time)
#((9:00am-9:30am),(10:00am,11:00am),(10:30am,11:30am))
#[(1,2),(3,6)]

def merge_ranges(meetings):

    merged_meetings = [null]

    #sort by start times.
    sorted_meetings = sorted(meetings)

    #initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:

        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        #if the current and last meetings overlap, use the lastest end time
        if(current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))

        else:
            merged_meetings.append((current_meeting_start, current_meeting_end))


    return merged_meetings
