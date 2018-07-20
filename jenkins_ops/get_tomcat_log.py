# import pickle
# import os
# import re
# import time
#
# class LogIncScaner(object):
#     def __init__(self, log_file, reg_ex, seek_file='/tmp/log-inc-scan.seek.temp'):
#         self.log_file = log_file
#         self.reg_ex = reg_ex
#         self.seek_file = seek_file
#
#     def scan(self):
#         seek = self._get_seek()
#         file_mtime = os.path.getmtime(self.log_file)
#         if file_mtime <= seek['time']:
#             print('file mtime not change since last scan')
#             seek['time'] = file_mtime
#             self._dump_seek(seek)
#             return []
#
#         file_size = os.path.getsize(self.log_file)
#         if file_size <= seek['position']:
#             print('file size not change since last scan')
#             seek['position'] = file_size
#             self._dump_seek(seek)
#             return []
#
#         print ('file changed,start to scan')
#         matchs = []
#         with open(self.log_file, 'rb') as logfd:
#             logfd.seek(seek['position'], os.SEEK_SET)
#             for match in re.finditer(self.reg_ex, logfd.read()):
#                 matchs.append(match)
#             seek = {'time': time.time(), 'position': logfd.tell()}
#             print (seek)
#             self._dump_seek(seek)
#         return matchs
#
#     def _get_seek(self):
#         seek = {'time': time.time(), 'position': 0}
#         if os.path.exists(self.seek_file):
#             with open(self.seek_file, 'rb') as seekfd:
#                 try:
#                     seek = pickle.load(seekfd)
#                 except:
#                     pass
#         print (seek)
#         return seek
#
#     def _dump_seek(self, seek):
#         with open(self.seek_file, 'wb') as seekfd:
#             pickle.dump(seek, seekfd)
#
#     def reset_seek(self):
#         self._dump_seek({'time': time.time(), 'position': 0})
#
#
# if __name__ == "__main__":
#     scaner = LogIncScaner('/var/log/messages', r'(\w+ \d+ \d+:\d+:\d+) .+?exception')
#     scaner.reset_seek()
#     while True:
#         matchs = scaner.scan()
#         for match in matchs:
#             print ('fond at:' + match.group(1) + ' content:' + match.group(0))
#         time.sleep(5)




# import os,time
# size=os.path.getsize('2.txt')
# print (size)
# seek = {'time': time.time(), 'position': 0}
# seek['position']=29
#
# with open('2.txt','r',encoding='utf-8') as f:
#     f.seek(seek['position'], os.SEEK_SET)
#     s=f.tell()
#     line=f.readline()
#     while line:
#         print(line, end = '')
#         line = f.readline()
#         time.sleep(1)
import os,time,sys
def read_log(path):
    fiel_size=os.path.getsize(path)
    print(fiel_size)
    seek={'positon':0}
    seek['positon']=fiel_size        #6606 71
    with open(path,'r') as f:
        f.seek(seek['positon'],os.SEEK_SET)
        line=f.readline()
        while line:
            #print(line, end = '')
            #line = f.readline()
            sys.stdout.write(line)
            time.sleep(1)
#read_log('catalina.out')
import paramiko
def exec_cmd(host,user,passwd,cm):
    ssh=paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #key=paramiko.RSAKey.from_private_key_file(key_file)
    ssh.connect(hostname=host,username=user,password=passwd,timeout=30)
    try:
        stdin,stdout,stderr=ssh.exec_command(cm)
        out_log=stdout.read().decode()
        err_log=stderr.read().decode()
        if len(out_log) !=0:
                # int(out_log)
            return (out_log)
            # if out_log.isalnum():
            #     return out_log
            # else:
            #     print ('\033[32mstdout:\033[0m'+out_log)
        if len(err_log) !=0:
            return  (err_log)
    except Exception as e:
        print (e)
    finally:
        ssh.close()
# ip='192.168.10.128'
# username='root'
# password='123456'
# action= 'start'
# size = exec_cmd(ip, 'root', '123456', "du -b /opt/tomcat/logs/catalina.out |awk '{print $1}'")
# s=exec_cmd('192.168.10.128', 'root', '123456', 'tail -n20 /opt/tomcat/logs/catalina.out')

# # time.sleep(3)
# cmd='python /opt/tomcat/logs/2.py %s' %size
# print(cmd)
# # log = exec_cmd('192.168.10.128', 'root', '123456',cmd)
