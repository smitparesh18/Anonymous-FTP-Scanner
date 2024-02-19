import ftplib

def anonLogin(hostname):
    try:
        ftp=ftplib.FTP(hostname)
        ftp.login('anonymous')
        print('\n [+] ' + str(hostname) + ' FTP Anonymous Login Successfull')
        ftp.quit()
        return True
    except Exception:
        print('\n [+] ' + str(hostname) + ' FTP Anonymous Login Failed')
        return False

if __name__ =='__main__':
    anonLogin('44.228.249.3')