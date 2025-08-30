#!/usr/bin/env python3


# serve_app.py

"""
Simple HTTP server to serve the demo app for testing purposes.
Run this before executing the Selenium tests.
"""
import http.server
import socketserver
import os
import sys
from pathlib import Path

PORT = 8000
DIRECTORY = "app"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def main():
    # Change to the project root directory
    project_root = Path(__file__).parent
    os.chdir(project_root)
    
    if not Path(DIRECTORY).exists():
        print(f"Error: {DIRECTORY} directory not found!")
        print("Make sure you're running this from the project root.")
        sys.exit(1)
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving demo app at http://localhost:{PORT}")
        print("Open http://localhost:8000/home.html in your browser")
        print("Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    main()
