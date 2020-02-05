from engine.database import database
import time

def delay_sync(t = 0.015):
    if t > 0:
        time.sleep(t)

'''
subscribe - publish communication 
'''
def get_value(tag, para = None):
    delay_sync()
    return database.get_value_by_tag(tag, para)


'''
Real-time communication
'''
def request(tag, para = None, wait_time = None):
    if wait_time == None:
        database.update_para_by_tag(tag, para)
    else:
        pass

    delay_sync()
    

'''
special usage
'''
def request_with_origin_script(script, wait_time = None):

    delay_sync()



