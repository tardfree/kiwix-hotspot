# -*- mode: python -*-

block_cipher = None

a = Analysis(['pibox-installer/__main__.py'],
             pathex=['.'],
             binaries=[('C:\Program Files\qemu\qemu-system-arm.exe', 'qemu'),
                       ('C:\Program Files\qemu\qemu-img.exe', 'qemu'),
                       ('C:\Program Files\qemu\iconv.dll', 'qemu'),
                       ('C:\Program Files\qemu\libfreetype-6.dll', 'qemu'),
                       ('C:\Program Files\qemu\libgnutlsxx-28.dll', 'qemu'),
                       ('C:\Program Files\qemu\liblzo2-2.dll', 'qemu'),
                       ('C:\Program Files\qemu\libpng16-16.dll', 'qemu'),
                       ('C:\Program Files\qemu\libasprintf-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libgailutil-3-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libgobject-2.0-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libmenuw6.dll', 'qemu'),
                       ('C:\Program Files\qemu\libssh2-1.dll', 'qemu'),
                       ('C:\Program Files\qemu\libatk-1.0-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libgcc_s_sjlj-1.dll', 'qemu'),
                       ('C:\Program Files\qemu\libgthread-2.0-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libncurses++w6.dll', 'qemu'),
                       ('C:\Program Files\qemu\libstdc++-6.dll', 'qemu'),
                       ('C:\Program Files\qemu\libbz2-1.dll', 'qemu'),
                       ('C:\Program Files\qemu\libgdk-3-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libgtk-3-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libncursesw6.dll', 'qemu'),
                       ('C:\Program Files\qemu\libtasn1-6.dll', 'qemu'),
                       ('C:\Program Files\qemu\libcairo-2.dll', 'qemu'),
                       ('C:\Program Files\qemu\libgdk_pixbuf-2.0-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libgtkreftestprivate-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libnettle-4.dll', 'qemu'),
                       ('C:\Program Files\qemu\libtiff-5.dll', 'qemu'),
                       ('C:\Program Files\qemu\libcairo-gobject-2.dll', 'qemu'),
                       ('C:\Program Files\qemu\libgio-2.0-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libharfbuzz-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libnghttp2-14.dll', 'qemu'),
                       ('C:\Program Files\qemu\libtiffxx-5.dll', 'qemu'),
                       ('C:\Program Files\qemu\libcairo-script-interpreter-2.dll', 'qemu'),
                       ('C:\Program Files\qemu\libglib-2.0-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libhogweed-2.dll', 'qemu'),
                       ('C:\Program Files\qemu\libp11-kit-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libturbojpeg-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libcurl-4.dll', 'qemu'),
                       ('C:\Program Files\qemu\libgmodule-2.0-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libintl-8.dll', 'qemu'),
                       ('C:\Program Files\qemu\libpanelw6.dll', 'qemu'),
                       ('C:\Program Files\qemu\libusb-1.0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libepoxy-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libgmp-10.dll', 'qemu'),
                       ('C:\Program Files\qemu\libjasper-1.dll', 'qemu'),
                       ('C:\Program Files\qemu\libpango-1.0-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libusbredirparser-1.dll', 'qemu'),
                       ('C:\Program Files\qemu\libexpat-1.dll', 'qemu'),
                       ('C:\Program Files\qemu\libgmpxx-4.dll', 'qemu'),
                       ('C:\Program Files\qemu\libjbig-2.dll', 'qemu'),
                       ('C:\Program Files\qemu\libpangocairo-1.0-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\SDL2.dll', 'qemu'),
                       ('C:\Program Files\qemu\libffi-6.dll', 'qemu'),
                       ('C:\Program Files\qemu\libgnurx-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libjbig85-2.dll', 'qemu'),
                       ('C:\Program Files\qemu\libpangoft2-1.0-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\zlib1.dll', 'qemu'),
                       ('C:\Program Files\qemu\libfontconfig-1.dll', 'qemu'),
                       ('C:\Program Files\qemu\libgnutls-28.dll', 'qemu'),
                       ('C:\Program Files\qemu\libjpeg-8.dll', 'qemu'),
                       ('C:\Program Files\qemu\libpangowin32-1.0-0.dll', 'qemu'),
                       ('C:\Program Files\qemu\libformw6.dll', 'qemu'),
                       ('C:\Program Files\qemu\libgnutls-openssl-27.dll', 'qemu'),
                       ('C:\Program Files\qemu\liblzma-5.dll', 'qemu'),
                       ('C:\Program Files\qemu\libpixman-1-0.dll', 'qemu')],
             datas=[('ui.glade', '.'),
                    ('pibox_ideascube_conf.py', '.'),
                    ('pibox-installer-vexpress-boot', 'pibox-installer-vexpress-boot')],
             hiddenimports=[],
             hookspath=['additional-hooks'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='launcher',
          debug=False,
          strip=False,
          upx=True,
          console=False,
          icon='pibox-installer-logo.ico',
          uac_admin=True)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='pibox-installer')
