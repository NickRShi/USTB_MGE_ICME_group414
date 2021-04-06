# -*- coding: utf-8 -*-
import sys
import os
#for mupif&&micress import 
mupif_dir=os.path.abspath(os.path.join(os.getcwd(), "../"))
micress_api=os.getcwd()

sys.path.append(mupif_dir)
sys.path.append(micress_api)

from mupif import *

import Physics.PhysicalQuantities as PQ
from shutil import copyfile

# MICRESS interface
from Micress import MICPropertyID

from Micress import micress
from Micress import clientConfig as cConf
import TimeStep
import APIError
import logging

from ValueType import ValueType

log = logging.getLogger()
'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('integers',type=float)
mode= parser.parse_args()
'''


def runMiccase(mic):
    
    time  = PQ.PhysicalQuantity(cConf.startTime, 's')
    
    dt=PQ.PhysicalQuantity(1, "s")
    
    istep = TimeStep.TimeStep(time, dt, PQ.PhysicalQuantity(cConf.targetTime, 's'), 's')
    
    '''
    if cConf.debug:
      print ("define background mesh for interpolation",
        cConf.nbX,cConf.nbY, cConf.lenX,cConf.lenY, cConf.originX, cConf.originY, cConf.originZ)
    if ( ( cConf.nbX > 0 ) and ( cConf.nbY > 0 ) ):
      nbX = cConf.nbX
      nbY = cConf.nbY
      lenX = cConf.lenX
      lenY = cConf.lenY
      origin = (cConf.originX, cConf.originY, cConf.originZ)
    elif ( ( cConf.nbX > 0 ) and ( cConf.nbZ > 0 ) ):
      print ("transfer XZ slice to XY coordinates")
      nbX = cConf.nbX
      nbY = cConf.nbZ
      lenX = cConf.lenX
      lenY = cConf.lenZ
      origin = (cConf.originX, cConf.originZ, cConf.originY)
    elif ( ( cConf.nbY > 0 ) and ( cConf.nbZ > 0 ) ):
      print ("transfer YZ slice to XY coordinates")
      nbX = cConf.nbY
      nbY = cConf.nbZ
      lenX = cConf.lenY
      lenY = cConf.lenZ
      origin = (cConf.originY, cConf.originZ, cConf.originX)
    else:
      raise APIError.APIError('no 2D slice recognized')
    
    bgMesh = util.generateBackgroundMesh(nbX,nbY,lenX,lenY,origin)
    
    # copy nodes for microstructure evaluation to an easy to handle list p
    p = []
    rd = 7
    for node in bgMesh.getVertices():
      if ( ( cConf.nbX > 0 ) and ( cConf.nbY > 0 ) ): # XY
        pNode = ( round(node[0],rd), round(node[1],rd), round(node[2],rd) )
      elif ( ( cConf.nbX > 0 ) and ( cConf.nbZ > 0 ) ): # XZ
        pNode = ( round(node[0],rd), round(node[2],rd), round(node[1],rd) )
      else: # YZ
        pNode = ( round(node[2],rd), round(node[0],rd), round(node[1],rd) )
      p.append(pNode)
    
    
    propLocation = Property.ConstantProperty( p, MICPropertyID.PID_RVELocation, ValueType.Vector, 'm')
    
    propT = Property.ConstantProperty( 555, MICPropertyID.PID_Temperature, ValueType.Scalar, 'K',  0 )

    propzG = Property.ConstantProperty( 0.0, MICPropertyID.PID_zTemperatureGradient, ValueType.Scalar, 'K/m',objectID=0 )
    '''
    propIE = Property.ConstantProperty( 6.4, MICPropertyID.PID_InterfacialEnergy, ValueType.Scalar, 'J/cm**2')
    '''  
    mic[0].setProperty(propLocation)
    
    mic[0].setProperty(propT)
    
    mic[0].setProperty(propzG)
    '''
    mic[0].setProperty(propIE)
    
    mic[0].solveStep(istep)

    pGS = mic[0].getProperty(MICPropertyID.PID_AvgGrainSizePerPhase,istep.getTargetTime())
    
    vGS = pGS.getValue()
    
    return vGS

def main():
    jobs = 0
    mic = []
    avgGrainSize = []
    jobsWorkdir = cConf.localWorkdir + "\\" + str(jobs)
    
    if ( not os.path.exists(jobsWorkdir) ):
        
        os.mkdir(jobsWorkdir)
        
    f=cConf.micressInputFiles
    filename = cConf.micressPrefix + '\\' + f            
    dest = jobsWorkdir + "\\" + f

    try:
        copyfile(filename,dest)
    except:
        print ("Error: file copy failed")
        print (f + ' -> ' + dest )
        sys.exit()
    
    try:
        mic.append(micress.micress(file='',workdir=jobsWorkdir))
    except Exception as e:
        log.error('jobsWorkdir=%s' % (jobsWorkdir) )
        log.exception(e)
    
    vGS=runMiccase(mic)
    avgGrainSize.append(vGS)

if __name__ == '__main__':
    try:
        main()
        log.info("Test OK")
    except:
        log.info("Test FAILED")
        sys.exit(1)