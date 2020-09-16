#!/bin/bash
python -u run.py data2 hsqldb | tee Data2/Data2_hsqldb.log
bloxbatch -db doop/last-analysis -query RealM | sort > Data2/hsqldb_M.facts
bloxbatch -db doop/last-analysis -query RealD0 | sort > Data2/hsqldb_D0.facts
bloxbatch -db doop/last-analysis -query RealD1 | sort > Data2/hsqldb_D1.facts
bloxbatch -db doop/last-analysis -query RealD3 | sort > Data2/hsqldb_D3.facts
rm -r doop/cache/*

#python -u run.py data2 batik | tee Data2/Data2_batik.log
#bloxbatch -db doop/last-analysis -query RealM | sort > Data2/xalan_M.facts
#bloxbatch -db doop/last-analysis -query RealD0 | sort > Data2/xalan_D0.facts
#bloxbatch -db doop/last-analysis -query RealD2 | sort > Data2/xalan_D2.facts
#bloxbatch -db doop/last-analysis -query RealD3 | sort > Data2/xalan_D3.facts

#rm -r doop/cache/*
#python -u run.py data2 sunflow | tee Data2/Data2_sunflow.log
#bloxbatch -db doop/last-analysis -query RealM | sort > Data2/xalan_M.facts
#bloxbatch -db doop/last-analysis -query RealD0 | sort > Data2/xalan_D0.facts
#bloxbatch -db doop/last-analysis -query RealD2 | sort > Data2/xalan_D2.facts
#bloxbatch -db doop/last-analysis -query RealD3 | sort > Data2/xalan_D3.facts

#rm -r doop/cache/*

#python -u run.py data2 jpc | tee Data2/Data2_jpc.log
#bloxbatch -db doop/last-analysis -query RealM | sort > Data2/xalan_M.facts
#bloxbatch -db doop/last-analysis -query RealD0 | sort > Data2/xalan_D0.facts
#bloxbatch -db doop/last-analysis -query RealD2 | sort > Data2/xalan_D2.facts
#bloxbatch -db doop/last-analysis -query RealD3 | sort > Data2/xalan_D3.facts

#rm -r doop/cache/*





