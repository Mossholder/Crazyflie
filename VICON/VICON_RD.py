import time
# Vicon DataStream
from vicon_dssdk import ViconDataStream

if __name__ == '__main__':
	# VICON client
	client = ViconDataStream.Client()

	# Connecting...
	print( 'Connecting' )
	while not client.IsConnected():
		print( '.' )
		client.Connect( '192.168.1.100:801' )
	client.EnableSegmentData()

	# Receiving Data
	try:
		while client.IsConnected():
			if client.GetFrame():
				axis=client.GetSegmentGlobalTranslation('crazyfly1','crazyfly1')
				print(axis[0][0])			# axis X
				print(axis[0][1])			# axis Y
				print(axis[0][1])			# axis Z
				time.sleep(1)

	except ViconDataStream.DataStreamException as e:
		print( 'Error', e )

