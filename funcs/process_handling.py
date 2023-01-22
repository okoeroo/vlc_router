import os, signal, subprocess, psutil, enum


def kill_proc(pid: int, sign: enum.IntEnum) -> None:
    print(f"Sending signal {sign} to parent PID: {pid}")
    os.kill(pid, sign)

def start_fresh_vlc(vlc_cmdline: str, pid_filename: str) -> None:
    # Reading PID
    try:
        vlc_pid = read_pid_from_file(pid_filename)
    except FileNotFoundError:
        print(f"Notice: PID file \"{pid_filename}\" not present.")
        vlc_pid = None 
    
    # Killing PID
    if vlc_pid is not None:
        try:
            os.kill(vlc_pid, signal.SIGTERM)
        except ProcessLookupError:
            print(f"Notice: PID \"{vlc_pid}\" was not found (nothing to kill).")

    # Starting VLC
    sub_proc = process_child_start(vlc_cmdline, True)

    # Store the PID in the file
    store_pid_to_file(sub_proc.pid, pid_filename)


def process_child_start(cmdline: str, start_new_session=False) -> subprocess.Popen: 
    if cmdline is None or cmdline == "":
        raise FileNotFoundError("cmdline is empty.")
    
    if not os.path.exists(cmdline.split()[0]):
        raise FileNotFoundError("Executable not found.")

    sub_proc = subprocess.Popen(cmdline.split(), start_new_session=start_new_session)
    return sub_proc


def read_pid_from_file(filename: str) -> int:
    if not os.path.exists(filename):
        raise FileNotFoundError("Error: the PID file does not exist")

    with open(filename, "r") as f:
        data = f.read()
        pid = int(data)
    return pid


def store_pid_to_file(pid: int, filename: str) -> bool:
    with open(filename, "w") as f:
        f.write(f"{pid}\n")


def kill_by_name(name_in_procname: str) -> bool:
    res = False
    for p in psutil.process_iter():
        if name_in_procname in p.name():
            p.terminate()
            p.wait()
            res = True
    return res
