import SimpleHTTPServer
import SocketServer
import sys
import socket
import os 


if len(sys.argv) > 1:
    try:
        PORT = int(sys.argv[1])
    except ValueError:
        PORT = -1
else:
    PORT = 8000

print "WinSimpleHTTP ----v1.1--------------------"
# Port range
# https://stackoverflow.com/questions/113224/what-is-the-largest-tcp-ip-network-port-number-allowable-for-ipv4#113228
if PORT < 2 or PORT > 65535:
    print "Invalid Port : " + str(PORT)
    print "Port must be 2-65535"
    print "------------------------------------------"
else:
    path = os.path.dirname(os.path.realpath(__file__))

    # How to get IP
    # https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
    ip = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]

    
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print path + " ---> " + ip + ":" + str(PORT)
    print "------------------------------------------"
    httpd.serve_forever()
