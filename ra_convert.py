import sys

if len(sys.argv) > 3:
	hours = float(sys.argv[1])
	mins_as_secs = float(sys.argv[2])*60
	total_secs = mins_as_secs + float(sys.argv[3])
	frac_hour = hours + total_secs/3600
	print("RA: {}H {}M {}S => {} hours".format(sys.argv[1], sys.argv[2], sys.argv[3], frac_hour))
print("finished") 
