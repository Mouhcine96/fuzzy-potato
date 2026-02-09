from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        msg = f"DevOps App is running | host={os.uname().nodename}\n"
        self.wfile.write(msg.encode())

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
