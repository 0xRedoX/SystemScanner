import platform
import psutil
import socket
print('''Enter the type of scan you want to do:>
(A) General Scan:
    Info about Oprating-System and More
(B) Full Scan:
    Info about OS,CPU,Memory''')
uinput = input('Enter Your Option Here: ')

def normalScan():
    os = platform.uname().system
    version = platform.uname().version
    arch = platform.uname().machine
    ip = socket.gethostbyname(socket.gethostname())
    print(
    f'''
    General Info:> {'-'*23}
    [*]Oprating System\t\t: {os}
    [*]System Version\t\t: {version}
    [*]Architecture\t: {arch}
    [*]IP Address\t: {ip}
    ======================================'''
    )

def fullSystemScan():
    os = platform.uname().system
    version = platform.uname().version
    arch = platform.uname().machine
    ip = socket.gethostbyname(socket.gethostname())
    physical = psutil.cpu_count(logical=False)
    threads = psutil.cpu_count(logical=True)
    cpufreqM = psutil.cpu_freq().min
    cpufreq = psutil.cpu_freq().max
    cpufreqC = psutil.cpu_freq().current
    memoryInfo = str(round(psutil.virtual_memory().total / (1023**3)))
    memoryInfoUsed = str(round(psutil.virtual_memory().percent))
    print(
    f'''
    General Info:> {'-'*23}
    [*]Oprating System\t\t: {os}
    [*]System Version\t\t: {version}
    [*]Architecture\t\t: {arch}
    [*]IP Address\t\t: {ip}
    ======================================
    CPU Info:> {'-'*27}
    [*]Physical Core\t\t: {physical} C
    [*]Thread Count\t\t: {threads} T
    [*]CPU Frequency(min)\t: {cpufreqM} Mhz
    [*]CPU Frequency(max)\t: {cpufreq} Mhz
    [*]CPU Friquency(current)\t: {cpufreqC} Mhz
    ======================================
    Memory Info:> {'-'*24}
    [*]Total Memory(RAM)\t: {memoryInfo}GB
    [*]Used Memory(RAM)\t\t: {memoryInfoUsed}% ({round(int(memoryInfoUsed) /int(memoryInfo)*100)}MB)
    ======================================'''
    )
if __name__=='__main__':
    if 'a' in uinput or 'A' in uinput:
        normalScan()
    elif 'B' in uinput or 'b' in uinput:
        fullSystemScan()
