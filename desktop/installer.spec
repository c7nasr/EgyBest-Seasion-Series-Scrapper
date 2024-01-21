# -*- mode: python ; coding: utf-8 -*-
import os
...
gooey_root = os.path.dirname(".")
# LOOK AT ME! I AM A TREE OBJECT
image_overrides = Tree('images', prefix='images')
...

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[("firebase.json", ".")],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          image_overrides,
          name='EgyBest Downloader V6.1',
          debug=False,
          strip=None,
          upx=True,
          console=False,
          icon=os.path.join(gooey_root, 'images', 'logo.ico'))

