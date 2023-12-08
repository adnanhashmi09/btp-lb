from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer


class HelloWorldHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, World!\n")


if __name__ == "__main__":
    server_address = ("0.0.0.0", 3033)
    httpd = TCPServer(server_address, HelloWorldHandler)

    print(f"Server running at http://{server_address[0]}:{server_address[1]}/")
    httpd.serve_forever()
