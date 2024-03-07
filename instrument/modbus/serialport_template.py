import serial, time # 安裝序列埠 -m pip install pyserial

serial_port = serial.Serial()
# serial.find()
serial_port.port ="COM6"
# 包柏 
serial_port.baudrate = 19200               # set baudrate
serial_port.bytesize = serial.EIGHTBITS    # number of bits per bytes
serial_port.parity = serial.PARITY_EVEN    # set prtiy check
serial_port.stopbits = serial.STOPBITS_ONE # number of stop bits

serial_port.timeout = 0.5       # non-block read 0.5s
serial_port.write_timeout = 0.5 # timeout for write 0.5s
serial_port.xonxoff = False     # disable software flow control
serial_port.rtscts = False      # disable hardware(RTS/CTS) flow control
serial_port.dsrdtr = False      # disable hardware(DSR/DTR) flow control
# 開啟序列埠 == == ==
try:
    serial_port.open()
except Exception as ex:
    print("open serial port error", str(ex))
    exit()

# 如果開啟等等
if serial_port.isOpen():
    try:
            serial_port.flushInput()  # flush input buffer
            serial_port.flushOutput() # flush output buffer
            # write byte data
            ## serial_port.write([78, 78, 78, 78, 78, 78, 78, 78])
            print("write 8 byte data: 78, 78, 78, 78, 78, 78, 78, 78")

            time.sleep(0.5)  #wait 0.5s
            
            #read 8 byte data
            response = serial_port.read(8)
            print("read 8 byte data:")
            print(response)

            serial_port.close()
    except Exception as ex:     
        print("communicating error " + str(ex))  
else:
    print("open serial port error")
    



"""_summary_
    python *.py
    write 8 byte data: 78, 78, 78, 78, 78, 78, 78, 78
    read 8 byte data:
    b'NNNNNNNN'
"""