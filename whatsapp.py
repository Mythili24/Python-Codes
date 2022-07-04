import pywhatkit as kit

try:
    kit.sendwhatmsg_instantly("+918861301826", "Happy New Year", 11, 35)
    print('Successfully sent')
except:
    print('Unexpected error')