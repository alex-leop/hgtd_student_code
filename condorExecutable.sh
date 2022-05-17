#!/bin/bash

nr=$1

cd /afs/cern.ch/work/a/aleopold/private/hgtd/student_code
## python setup??
python loopOverFiles.py $nr

if [ $? -ne 0 ]
then
  echo "FAIL"
else
  echo "SUCCESS"
fi
