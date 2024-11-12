from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
     <body>
        <hl align="center">DEVICE SPECIFICATIONS<i>(GOWTHAM GT 24901330</i>)</hl>
        <ol>
        <li>Device name - DESKTOP-MOHHBTU</li>
        <li>Procssor - 13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz</li>
        <li>RAM-16gb</li>
        <li>Device ID - 15EEA3B2-7EF5-4DEC-903D-577382C3C005</li>
        <li>System Type - 64 bit </li>
    <body>
</html>    
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()