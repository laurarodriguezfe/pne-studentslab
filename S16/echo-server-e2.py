import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse


PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path

        if path == "/":
            contents = Path('html/form-e2.html').read_text()
            self.send_response(200)

        elif path == "/echo":
            arguments = parse_qs(url_path.query)
            msg = arguments.get("msg", [""])[0]

            if "upper" in arguments:
                msg = msg.upper()

            contents = f"""
            <!DOCTYPE html>
            <html>
            <body>
                <h1>Echoing the received message:</h1>
                <p>{msg}</p>
                <a href="/">Main page</a>
            </body>
            </html>
            """

            self.send_response(200)

        else:
            contents = Path('html/error.html').read_text()
            self.send_response(404)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()

        self.wfile.write(str.encode(contents))

        return

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()