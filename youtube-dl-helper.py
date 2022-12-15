import subprocess
import sys


outputobj = subprocess.run(['youtube-dl', '-x', sys.argv[1]], stdout=subprocess.PIPE)

output = outputobj.stdout

print(output)
index = 0

while True:
    if (outputobj.returncode == 1):
        s = ''.join(map(chr, outputobj.stdout))

        index += int(s.split()[-7])
        print(index)
        outputobj = subprocess.run(['youtube-dl', '-x', '--playlist-start', str(index), sys.argv[1]], stdout=subprocess.PIPE)
    else:
        break
