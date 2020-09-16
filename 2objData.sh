#!/bin/bash

python -u run.py data1 eclipse | tee 2objData/2objData_eclipse.log
rm -r doop/cache/*

python -u run.py data1 xalan | tee 2objData/2objData_xalan.log
rm -r doop/cache/*

python -u run.py data1 chart | tee 2objData/2objData_chart.log
rm -r doop/cache/*

python -u run.py data1 bloat | tee 2objData/2objData_bloat.log
rm -r doop/cache/*

python -u run.py data1 findbugs | tee 2objData/2objData_findbugs.log
rm -r doop/cache/*

python -u run.py data1 jedit | tee 2objData/2objData_jedit.log
rm -r doop/cache/*

python -u run.py data1 briss | tee 2objData/2objData_briss.log
rm -r doop/cache/*

python -u run.py data1 fop | tee 2objData/2objData_fop.log
rm -r doop/cache/*

python -u run.py data1 batik | tee 2objData/2objData_batik.log
rm -r doop/cache/*

python -u run.py data1 checkstyle | tee 2objData/2objData_checkstyle.log
rm -r doop/cache/*

python -u run.py data1 sunflow | tee 2objData/2objData_sunflow.log
rm -r doop/cache/*

python -u run.py data1 jpc | tee 2objData/2objData_jpc.log
rm -r doop/cache/*




