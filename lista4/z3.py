import math

def rad_deg(rad=None,deg=None):
	if rad != None:
		degree = math.degrees(rad)
	else:
		degree = None
	if deg != None:
		radian = math.radians(deg)
	else:
		radian = None
	if degree is None:
		result = radian
	elif radian is None:
		result = degree 
	else:
		result = radian,degree
	
	return result
	
stopnie = rad_deg(rad=1.5)
radiany = rad_deg(deg=90)

