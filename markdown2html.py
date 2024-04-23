#!/usr/bin/python3
"""LOLIPOP"""
import sys
import os

if len(sys.argv) <= 2:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

if not os.path.exists(sys.argv[1]):
    print(f"Missing {sys.argv[1]}")
    exit(1)

print()
exit(0)
