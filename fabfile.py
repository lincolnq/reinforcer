from fabric.api import *

env.use_ssh_config = True
if len(env.hosts) == 0:
    env.hosts = ['rpi']

def step(dist=-512):
    put('step.py', '')
    sudo('python step.py %s' % (dist,))

