#!/bin/bash

python -u run.py data2 eclipse | tee 3objData/3objData_eclipse.log
rm -r doop/cache/*

python -u run.py data2 xalan | tee 3objData/3objData_xalan.log
rm -r doop/cache/*

python -u run.py data2 chart | tee 3objData/3objData_chart.log
rm -r doop/cache/*

python -u run.py data2 bloat | tee 3objData/3objData_bloat.log
rm -r doop/cache/*

python -u run.py data2 findbugs | tee 3objData/3objData_findbugs.log
rm -r doop/cache/*

python -u run.py data2 jedit | tee 3objData/3objData_jedit.log
rm -r doop/cache/*

python -u run.py data2 briss | tee 3objData/3objData_briss.log
rm -r doop/cache/*

python -u run.py data2 fop | tee 3objData/3objData_fop.log
rm -r doop/cache/*

python -u run.py data2 batik | tee 3objData/3objData_batik.log
rm -r doop/cache/*

python -u run.py data2 checkstyle | tee 3objData/3objData_checkstyle.log
rm -r doop/cache/*

python -u run.py data2 sunflow | tee 3objData/3objData_sunflow.log
rm -r doop/cache/*

python -u run.py data2 jpc | tee 3objData/3objData_jpc.log
rm -r doop/cache/*

python -u run.py data2 hsqldb | tee 3objData/3objData_hsqldb.log
rm -r doop/cache/*

python -u run.py data2 jython | tee 3objData/3objData_jython.log
rm -r doop/cache/*


