# Vicon DataStream
from vicon_dssdk import ViconDataStream

client = ViconDataStream.Client()
 
print( 'Connecting' )
while not client.IsConnected():
    print( '.' )
    client.Connect( '192.168.1.100:801' )
 
try:
  while client.IsConnected():
    if client.GetFrame():
      print( 'Frame Number', client.GetFrameNumber() )

   
except ViconDataStream.DataStreamException as e:
  print( 'Error', e )


