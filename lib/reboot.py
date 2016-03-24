from subprocess import Popen, PIPE

def reboot_domogik():
    # build the reboot script
    tmp_script = "/tmp/reboot_dmg.sh"
    script = """#!/bin/bash
        sleep 10
        sudo /etc/init.d/domogik restart"""
    fp = open(tmp_script, "w+")
    fp.write(script)
    fp.close()
    run_script(tmp_script)
    
def reboot_domoweb():
    # build the reboot script
    tmp_script = "/tmp/reboot_dmw.sh"
    script = """#!/bin/bash
        sleep 10
        sudo /etc/init.d/domoweb restart"""
    fp = open(tmp_script, "w+")
    fp.write(script)
    fp.close()
    run_script(tmp_script)
    
def run_script(script):
    # run a script
    cmd = "cd /tmp/ && nohup /bin/bash {0} &".format(script)
    subp = Popen(cmd, shell=True)
    pid = subp.pid
    subp.communicate()
