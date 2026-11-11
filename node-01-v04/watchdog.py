#!/usr/bin/env python3
"""Independent local watchdog for Artefakt Node 01. No network or credentials."""
import json, os, pathlib, signal, subprocess, sys, time, fcntl
BASE=pathlib.Path.home()/'artefakt-node-01'
BOOT=BASE/'node.py'
HEART=BASE/'heartbeat.json'
LOG=BASE/'watchdog.jsonl'
LOCK=BASE/'watchdog.lock'
INTERVAL=120
STALE=300
COOLDOWN=600
MAX_RESTARTS_HOUR=4
def log(action,**details):
 with LOG.open('a') as f: f.write(json.dumps({'timestamp':time.time(),'action':action,**details})+'\n')
def age():
 try: return time.time()-HEART.stat().st_mtime
 except FileNotFoundError: return float('inf')
def alive(pid):
 try: os.kill(pid,0); return True
 except (OSError,ValueError,TypeError): return False
def pid():
 try: return int((BASE/'worker.pid').read_text().strip())
 except (FileNotFoundError,ValueError): return None
def start():
 with (BASE/'worker.log').open('a') as output:
  proc=subprocess.Popen([sys.executable,'-u',str(BOOT)],stdin=subprocess.DEVNULL,stdout=output,stderr=subprocess.STDOUT,start_new_session=True)
 (BASE/'worker.pid').write_text(str(proc.pid)+'\n')
 log('start',pid=proc.pid)
def main():
 BASE.mkdir(exist_ok=True)
 with LOCK.open('w') as lock:
  try: fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  except BlockingIOError: return
  restarts=[]
  while True:
   now=time.time()
   restarts=[t for t in restarts if now-t<3600]
   p=pid()
   stale=age()>STALE
   if (not alive(p)) or stale:
    if len(restarts)>=MAX_RESTARTS_HOUR:
     log('rate_limited',pid=p,stale=stale)
    elif not restarts or now-restarts[-1]>=COOLDOWN:
     if alive(p):
      try: os.kill(p,signal.SIGTERM)
      except ProcessLookupError: pass
      time.sleep(3)
      if alive(p):
       log('termination_failed',pid=p)
       time.sleep(INTERVAL)
       continue
     start()
     restarts.append(now)
   time.sleep(INTERVAL)
if __name__=='__main__': main()
