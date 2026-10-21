#!/usr/bin/env python3
"""Rebuild AI Driver ChatGPT ZIP packages locally without changing the repository.
Output is isolated and refuses to overwrite existing files."""
import argparse, hashlib, json
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_STORED

EDITION=Path('chatgpt/ai-driver')
VERSION='v0.1.12-poc13'
FILES=[
 '.codex-plugin/plugin.json','INSTALL.ja.md','LICENSE','README.md','plugin.json',
 'skills/ai-driver/SKILL.md',
 'skills/ai-driver/references/chatgpt-library-adapter.md',
 'skills/ai-driver/references/conflict-rules.md',
 'skills/ai-driver/references/original-requirements.ja.md',
 'skills/ai-driver/references/publication-privacy.md',
 'skills/ai-driver/references/requirements.md',
 'skills/ai-driver/references/state-contract.md',
 'skills/ai-driver/templates/state-template.md',
]

def sha(data): return hashlib.sha256(data).hexdigest()
def build(root,out,name,pairs):
    target=out/name
    if target.exists(): raise FileExistsError('Existing output: '+str(target))
    expected={}
    with ZipFile(target,'w',allowZip64=False) as z:
        for source,member in sorted(pairs,key=lambda p:p[1]):
            src=root/EDITION/source
            if not src.is_file() or src.is_symlink(): raise ValueError('Missing or unsafe source: '+str(src))
            payload=src.read_bytes(); expected[member]=sha(payload)
            info=ZipInfo(member,date_time=(2020,1,1,0,0,0))
            info.compress_type=ZIP_STORED; info.external_attr=0o100644 << 16
            z.writestr(info,payload,compress_type=ZIP_STORED)
    with ZipFile(target) as z:
        members=z.namelist()
        if sorted(members)!=sorted(expected) or len(members)!=len(expected): raise ValueError('ZIP member mismatch')
        if z.testzip() is not None: raise ValueError('CRC failure')
        for member in members:
            if sha(z.read(member))!=expected[member]: raise ValueError('Source mismatch: '+member)
    return {'name':target.name,'entries':len(expected),'sha256':sha(target.read_bytes()),'CRC':'PASS'}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo-root',type=Path,required=True)
    parser.add_argument('--out-dir',type=Path,required=True)
    args=parser.parse_args(); root=args.repo_root.resolve(); out=args.out_dir.resolve()
    if not (root/EDITION/'skills/ai-driver/SKILL.md').is_file(): raise SystemExit('Missing source checkout')
    if out==(root/EDITION).resolve() or (root/EDITION).resolve() in out.parents: raise SystemExit('Output inside source forbidden')
    out.mkdir(parents=True,exist_ok=True)
    skill=[(p,'ai-driver/'+p[len('skills/ai-driver/'):]) for p in FILES if p.startswith('skills/ai-driver/')]
    skill.append(('LICENSE','ai-driver/LICENSE'))
    result=[build(root,out,f'ai-driver-chatgpt-plugin-{VERSION}.zip',[(p,p) for p in FILES]),
            build(root,out,f'ai-driver-chatgpt-skill-{VERSION}.zip',skill)]
    print(json.dumps({'status':'LOCAL_ONLY_NOT_PUBLISHED','packages':result},indent=2))

if __name__=='__main__': main()
