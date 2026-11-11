#!/usr/bin/env python3
import json,time,datetime,pathlib,urllib.request,signal
base=pathlib.Path(__file__).resolve().parent
running=True
def stop(*_):
 global running
 running=False
signal.signal(signal.SIGTERM,stop)
signal.signal(signal.SIGINT,stop)
while running:
 cfg=json.loads((base/'config.json').read_text())
 results={}
 for url in cfg['urls']:
  if not url.startswith('https://'): continue
  start=time.monotonic()
  try:
   with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'ArtefaktNode01/0.1'}),timeout=12) as response:
    code=response.status
   results[url]={'ok':200<=code<400,'status':code,'ms':round((time.monotonic()-start)*1000)}
  except Exception as e:
   results[url]={'ok':False,'error':type(e).__name__}
 report={'node':'artefakt-node-01','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':results}
 (base/'status.json.tmp').write_text(json.dumps(report,indent=2))
 (base/'status.json.tmp').replace(base/'status.json')
 with (base/'events.jsonl').open('a') as f:f.write(json.dumps(report)+'\n')
 print(json.dumps(report),flush=True)
 for _ in range(max(60,int(cfg.get('interval_seconds',900)))):
  if not running:break
  time.sleep(1)
