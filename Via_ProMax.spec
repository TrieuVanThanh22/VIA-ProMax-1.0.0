# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

pillow_datas, pillow_binaries, pillow_hidden = collect_all('PIL')
dnd_datas, dnd_binaries, dnd_hidden = collect_all('tkinterdnd2')

a = Analysis(
    ['Via_ProMax.py'],
    pathex=[],
    binaries=pillow_binaries + dnd_binaries,
    datas=pillow_datas + dnd_datas,
    hiddenimports=pillow_hidden + dnd_hidden,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Via_ProMax',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
)
