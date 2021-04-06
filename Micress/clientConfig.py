"""
This configuration file provides necessary information for the
top-level scenario script, i.e. CIGS_example.py:

- local working directory
- input files for individual applications
- number of used interfaces
- debug message settings
- simulation time
- start emissivity for X-Stream
- interpolation surface mesh settings
- monitor files

See source code comments for more information.

"""

import sys
import os
sys.path.append('../../..') # Mupif path
import Pyro4
Pyro4.config.SERIALIZER = "pickle"
Pyro4.config.PICKLE_PROTOCOL_VERSION = 2  # to work with python 2.x and 3.x
Pyro4.config.SERIALIZERS_ACCEPTED = {'pickle'}
Pyro4.config.HOST = 'localhost'
# the working directory will contains some pre-calculated results
# from X-Stream and MICRESS for this example
if ( sys.platform.lower().startswith('lin') ):
  localWorkdir = "./workbench"
else:
  localWorkdir = os.path.abspath(os.path.join(os.getcwd(),"Micress/workbench"))

# input subdirectories relativ to working directory of the top-level script, i.e.
# file location of Precursor_B.txt is "./in_qFact/Precursor_B.txt"
micressPrefix = os.path.abspath(os.path.join(os.getcwd(),"Micress/micress_dir"))
micressInputFiles = ('3Graingrowth_dri.template')


# number of application interfaces
# In this example, these numbers have to match to the setting used for pre-calculating data.
# Just to find the data.

micressJobs = 1

# debug output settings
debug = False  # while running the test case itself
debugComm = False  # while setting up the communication environment (SSH tunnels, job allocation, etc.)
mupifLogging = False  # screen output for Mupif internal logging (e.g. from PyroUtil )

startTime = 2.0 # simulation's start time in seconds
targetTime = 2.0 # simulations's target time in seconds
           

# mesh definition of the 2D plane of glass substrate's surface
# The nodes of this mesh will be serve as RVE locations on a microstructural level
nbX = 3 # number of nodes
nbY = 3
nbZ = 0
lenX = 0.03 # length in meter
lenY = 0.03
lenZ = 0
originX = -0.015 # origin at the corner, coordinates in meter
originY = -0.015
originZ = 0.0 # current Z coordinate for glas substrate surface

nshost = 'mech.FSV.CVUT.CZ'   # NameServer - do not change
nsport = 9090  # NameServer's port - do not change
hkey = 'mmp-secret-key'  # Password for accessing nameServer and applications
nathost = 'localhost'  # NatHost of local computer - do not change
serverNathost = 'localhost'  # NatHost of local computer - do not change

server = 'mmpserver.erve.vtt.fi'
daemonHost = 'mmpserver.erve.vtt.fi'  # IP of server
hostUserName = 'elemim'  # 'mmp'#User name for ssh connection

# Edit these paths for your SSH-client and location of a private key
if(sys.platform.lower().startswith('win')):  # Windows ssh client
    sshClient = 'C:\\Program Files\\Putty\\putty.exe'
    options = '-i C:\\msys64\\home\\otolli\\.ssh\\putty_private.ppk'
    sshHost = ''
else:  # Unix ssh client
    sshClient = 'ssh'
    options = '-oStrictHostKeyChecking=no'
    sshHost = ''

# jobManager records to be used in scenario
# format: (jobManPort, jobManNatport, jobManHostname, jobManUserName,jobManDNSName)

mieSolverJobManRec = (44360, 5557, 'mmpserver.erve.vtt.fi',
                      hostUserName, 'Mupif.JobManager@MMPMie')

tracerSolverJobManRec = (44362, 5556, 'mmpserver.erve.vtt.fi',
                         hostUserName, 'Mupif.JobManager@Raytracer')


comsolSolverJobManRec = (44363, 5558, 'mmpserver.erve.vtt.fi',
                         hostUserName, 'Mupif.JobManager@MMPComsolDummy')

# client ports used to establish ssh connections (nat ports)
jobNatPorts = range(4000, 4019)