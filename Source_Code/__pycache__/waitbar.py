import sys
import time
import urllib.request

def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    print(duration)
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
    (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()

def save(url, filename):
    urllib.request.urlretrieve(url, filename, reporthook)

save('https://github.com/HowcanoeWang/Floraecite/raw/master/Source_Code/Floraecite(Beta1.7.0).exe','test.exe')