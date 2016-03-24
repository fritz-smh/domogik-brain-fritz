from subprocess import Popen, PIPE

def count_errors_in_logs(log, path, when = "TODAY"):
    if when == "TODAY":
        date_args = "'+%Y-%m-%d'"
    elif when == "YESTERDAY":
        date_args = "'+%Y-%m-%d' -d -1day"
    else:
        return "mauvaise date" # oui, crado, je sais ;)

    cmd = "grep \"$(date {0}).*ERROR\" {1} | wc -l".format(date_args, path)
    log.debug(u"Count errors with command : {0}".format(cmd))
    subp = Popen(cmd, shell=True, stdout=PIPE)
    pid = subp.pid
    out = subp.communicate()[0].strip()
    return out
