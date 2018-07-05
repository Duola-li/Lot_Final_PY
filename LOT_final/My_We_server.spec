# -*- mode: python -*-

block_cipher = None


a = Analysis(['My_We_server.py'],
             pathex=['C:\\Users\\Octan3\\Desktop\\LOT_final'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='My_We_server',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
