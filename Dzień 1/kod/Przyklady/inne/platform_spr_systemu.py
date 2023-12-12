import sys

if sys.platform.startswith('linux'):
    print("Linux")
elif sys.platform.startswith('win'):
    print("Windows")
elif sys.platform.startswith('darwin'):
    print("macOS")
