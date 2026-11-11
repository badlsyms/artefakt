#!/usr/bin/env python3
import datetime as dt, fcntl, json, os, signal, time
from pathlib import Path
from urllib.request import Request, urlopen
BASE=Path.home()/'artefakt-node-01'
STOP=False
def stop(*_):
 global STOP
 STOP=True
def utc(): return dt.datetime.now(dt.timezone.utc).isoformat()
def atomic(path,obj):
 tmp=path.with_suffix(path.suffix+'.tmp')
 tmp.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
 tmp.replace(path)
def check(url):
 start=time.monotonic()
 try:
  with urlopen(Request(url,headers={'User-Agent':'ArtefaktNode01/0.3'}),timeout=12) as r: status=r.status
  return {'ok':200<=status<400,'status':status,'ms':round((time.monotonic()-start)*1000)}
 except Exception as e: return {'ok':False,'error':type(e).__name__}
def main():
 BASE.mkdir(parents=True,exist_ok=True)
 lock=(BASE/'worker.lock').open('w')
 try: fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
 except BlockingIOError:
  print('Node already running',flush=True)
  return
 signal.signal(signal.SIGTERM,stop)
 signal.signal(signal.SIGINT,stop)
 cfg=json.loads((BASE/'config.json').read_text())
 interval=max(60,int(cfg.get('interval_seconds',900)))
 urls=[u for u in cfg.get('urls',[]) if isinstance(u,str) and u.startswith('https://')]
 next_run=time.monotonic()
 count=0
 while not STOP:
  now=time.monotonic()
  if now>=next_run:
   delay=round(max(0,now-next_run),2)
   count+=1
   report={'node':'artefakt-node-01','version':'0.3','utc':utc(),'pid':os.getpid(),'sequence':count,'schedule_delay_seconds':delay,'checks':{u:check(u) for u in urls}}
   atomic(BASE/'status.json',report)
   with (BASE/'events.jsonl').open('a') as f: f.write(json.dumps(report)+'\n')
   print(json.dumps(report),flush=True)
   next_run=time.monotonic()+interval
  atomic(BASE/'heartbeat.json',{'node':'artefakt-node-01','version':'0.3','utc':utc(),'pid':os.getpid(),'next_check_in_seconds':round(max(0,next_run-time.monotonic()))})
  end=time.monotonic()+min(60,max(1,next_run-time.monotonic()))
  while not STOP and time.monotonic()<end: time.sleep(min(1,max(.01,end-time.monotonic())))
if __name__=='__main__': main()
