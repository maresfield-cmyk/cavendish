#!/usr/bin/env python3
"""Local preview server that mirrors how the site is served in production.

Plain `python3 -m http.server` does not resolve extension-less URLs, so `/casino`
404s locally even though it works on the real host. This adds the two behaviours
production gives us: `/<slug>` resolves to `<slug>.html`, and anything genuinely
missing renders `404.html`.

    python3 serve.py [port]      # defaults to 8000
"""

import os
import sys
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler

ROOT = os.path.dirname(os.path.abspath(__file__))


class CleanURLHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        local = super().translate_path(path)
        if not os.path.exists(local) and not local.endswith(".html"):
            candidate = local.rstrip("/") + ".html"
            if os.path.isfile(candidate):
                return candidate
        return local

    def send_error(self, code, message=None, explain=None):
        page = os.path.join(ROOT, "404.html")
        if code == 404 and os.path.isfile(page):
            with open(page, "rb") as fh:
                body = fh.read()
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)
            return
        super().send_error(code, message, explain)


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    handler = partial(CleanURLHandler, directory=ROOT)
    print(f"Serving {ROOT} at http://localhost:{port}/  (Ctrl-C to stop)")
    try:
        HTTPServer(("", port), handler).serve_forever()
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
