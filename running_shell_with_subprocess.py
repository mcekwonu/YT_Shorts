#
#  www.youtube.com/@mersthub_mentors
#

import subprocess

result = subprocess.run(["python3", "-V"],
                        capture_output=True,
                        text=True)

print(f"OUTPUT: {result.stdout}\n"
      f"Return Code:{result.returncode}")