import stem.process
import time
def __logsTorInstance(log):
	print(log)
torConfig = {'ControlPort': '9051', 'SocksPort' : '5000'}
torProcess = stem.process.launch_tor_with_config(config = torConfig, tor_cmd="/home/adastra/tools/Hacking/anon/tor-0.4.6.8/src/app/tor", init_msg_handler=__logsTorInstance)
time.sleep(5)
if torProcess > 0:
	print("TOR Process PID %s " %(torProcess.pid))
