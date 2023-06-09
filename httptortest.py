from requests_tor import RequestsTor
import sys

rt = RequestsTor(tor_ports=(9050,), tor_cport=9051)
with open(sys.argv[1], "r") as fh:
    with open(f"{sys.argv[1]}.csv", "w") as fw:

        for line in fh:
            line = line.rstrip()
            try:
                http = str(rt.get(f'http://{line}'))
            except:
                http = '<Unreachable>'

            try:
                https = str(rt.get(f'https://{line}'))
            except:
                https = '<Unreachable>'

            fw.write(f'----------------------------------\n')
            fw.write(f'http://{line}-{http}\n')
            fw.write(f'https://{line}-{https}\n')
            print(f'http://{line}-{http}')
            print(f'https://{line}-{https}')
