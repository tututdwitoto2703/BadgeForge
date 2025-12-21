# this is only for quick development not a dependency when releasing prod
# live reload on saving (getmtime(modif time))

import os, time
import subprocess, sys

file_loc = "./test.py"
# i forgot to add sys.executable F
process = subprocess.Popen([sys.executable, file_loc])
last_mtime = os.path.getmtime(file_loc)
while True:
    try:
        time.sleep(1)
        curr_mtime = os.path.getmtime(file_loc)
        if curr_mtime != last_mtime:
            try:
                last_mtime = curr_mtime
                process.terminate()
                process.wait() # i am adding this because terminate doesnt wait [zombie process issue]
                print("changes")
            # this reload even works when eror but processlookuperror is still possible
            except ProcessLookupError:
                print("[!!!] IMPORTANT - somehow the process ended itself!?!??! issue with the test.py code fix errors")
            process = subprocess.Popen([sys.executable, file_loc])
    except KeyboardInterrupt:
        print("[!!]= Progran exitting =[!!]")
        try:
            process.terminate()
        except ProcessLookupError:
            pass
        process.wait()
        break