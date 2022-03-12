import bluetooth

bd_addr = ""

port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()
