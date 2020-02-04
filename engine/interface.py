from engine.database import database
'''
subscribe - publish communication 
'''
def get_value(tag, para = None):
	return database.get_value_by_tag(tag, para)


'''
Real-time communication
'''
def request(tag, para = None, wait_time = None):
	if wait_time == None:
	    database.update_para_by_tag(tag, para)
	else:
		pass
	

'''
special usage
'''
def request_with_origin_script(script, wait_time = None):
	pass




