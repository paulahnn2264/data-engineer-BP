#README:
#all code written within the suggested under hour timeline
#that being said, i looked for all general cases, leaving out easy to catch edges and checks
#looked for conceptual finding of how i could create the table that you were looking for

#given more tiem i would probably try to use more df/pandas functions to increase speed and
#make things a little easier and simple

#i had a little bit of consuion of the relationship of the two files and how they work, but this
#is something id love to talk about at a later time

#none of this code was checked for compliation or tested

import csv
import numpy as np
import pandas

current_status = {}

df_table_history = pd.read_csv("table-history.csv")
df_table_history.sort_values(by='postdate',inplace=True)

df_status_change = pd.read_csv("status-change.csv")
df_status_change.sort_values(by='postdate',inplace=True)

##-------##
#below seem to be accessible using only status_change based on status

member_status = {}
for row in df_status_change:
    member_status[row['customer_id']] = row

#check for freeze
for member in member_status:
    if member['status'] = 'FREEZE':
        current_status[member['member_id']] = [member['start_date'], member['end_date'], 'freeze']


#check for terminate
for member in member_status:
    if member['status'] = 'TERMINATE':
        current_status[member['member_id']] = [member['start_date'], member['end_date'], 'cancel']


##-------##

#check for guest/member/punch
for row in df_table_history:
    changes = row['changes'].split('@#@#@#')
    for transaction in changes:
        transaction.split('-^!^!^')
        for i in transaction:
            attribute = i[0]
            old_val = i[1]
            new_val = i[2]
            #do some error checking here

            #check for expire

            #check for freezes
            if (attribute = 'current_status') and (old_val = 'OK') and (new_val = 'FROZEN'):
                current_status[row['customer_id']] = ['', member['post_date'], 'freeze']

            #member to punch card cancels
            if (attribute = 'customer_type') and (old_val = 'MEMBER') and (new_val = 'PUNCH CARD'):
                current_status[row['customer_id']] = ['', member['post_date'], 'expire']\

            #cross reference other DF to see if there are start dates there? not sure if they're related
            #otherwise check sequentially by date to see if there is a previous history of them turning into a member, which should be inputted into the dictionary first

            #coudln't find example of membership just expiring (no payment, end of annual, etc)
            #but in that case we would find the attribute of and i'm assuming it would check bill date and go null or something
            #this would trigger a check that would mark it as expire
            #if there's no membership_form_of_payment and a next due date of payment that could be one way for an expire entry
            #if the last_billed_date is over a month before the postdate of the row, that could also be a sign of expiration

            #validation to make sure members that I found to be active aren't included in the current_status dictionary


        #thanks austin - i know this is a little sloppy and also late, but i really wanted to test my 1hour limit and see what i could do with it
        #look forward to talking with you later
