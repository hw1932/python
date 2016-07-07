import ftplib
import os
import socket

def main():
    host = 'ftp.mozilla.org'
    dirn = 'pub/mozilla.org/webtools'
    file = 'bugzilla-LATEST.tar.gz'
    try:
        f = ftplib.FTP(host)
    except (socket.error, socket.gaierror) as e:
        print('ERROR:cannot reache "%s"' % host)
        return
    print('*** Connected to host "%s"' % host)

    try:
        f.login()
    except ftplib.error_perm:
        print('Error:cannot login anonymously')
        f.quite()
        return
    print('***logged in as "anonymous"')

    try:
        f.cwd(dirn)
    except ftplib.error_perm:
        print('Error:cannot cd to "%S"' % dirn)
        f.quit()
        return
    print('***change to "%S" folder' % dirn)

    try:
        f.retrbinary('RETR %s' % file,
                     open(file, 'wb').write)
    except ftplib.error_perm:
        print('Error:cannot read file"%s"' % file)
        os.unlink(file)

    else:
        print('***downloaded "%s" to cwd' % file)
    f.quit()
    return

import ftplib, os, socket



def main2():
    host = 'ftp.python.org'
    dirn = 'opt/cwd/aa'
    file = 'filename.tar.gz'
    f = ftplib.FTP(host)
    f.login()
    f.cwd(dirn)
    w = open(dirn,'wb')
    f.retrbinary('retr %s' %file,w.write())
    w.close()
    f.close()

if __name__ == '__main__':
    main()
