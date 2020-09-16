#!/bin/bash
python -u run.py data2 eclipse | tee Data2/Data2_eclipse.log
bloxbatch -db doop/last-analysis -query RealM | sort > Data2/eclipse_M.facts
bloxbatch -db doop/last-analysis -query RealD0 | sort > Data2/eclipse_D0.facts
bloxbatch -db doop/last-analysis -query RealD2 | sort > Data2/eclipse_D2.facts
bloxbatch -db doop/last-analysis -query RealD3 | sort > Data2/eclipse_D3.facts
rm -r doop/cache/*

python -u run.py data2 xalan | tee Data2/Data2_xalan.log
bloxbatch -db doop/last-analysis -query RealM | sort > Data2/xalan_M.facts
bloxbatch -db doop/last-analysis -query RealD0 | sort > Data2/xalan_D0.facts
bloxbatch -db doop/last-analysis -query RealD2 | sort > Data2/xalan_D2.facts
bloxbatch -db doop/last-analysis -query RealD3 | sort > Data2/xalan_D3.facts
rm -r doop/cache/*

python -u run.py data2 chart | tee Data2/Data2_chart.log
bloxbatch -db doop/last-analysis -query RealM | sort > Data2/chart_M.facts
bloxbatch -db doop/last-analysis -query RealD0 | sort > Data2/chart_D0.facts
bloxbatch -db doop/last-analysis -query RealD2 | sort > Data2/chart_D2.facts
bloxbatch -db doop/last-analysis -query RealD3 | sort > Data2/chart_D3.facts

rm -r doop/cache/*

python -u run.py data2 bloat | tee Data2/Data2_bloat.log
bloxbatch -db doop/last-analysis -query RealM | sort > Data2/bloat_M.facts
bloxbatch -db doop/last-analysis -query RealD0 | sort > Data2/bloat_D0.facts
bloxbatch -db doop/last-analysis -query RealD2 | sort > Data2/bloat_D2.facts
bloxbatch -db doop/last-analysis -query RealD3 | sort > Data2/bloat_D3.facts

rm -r doop/cache/*

python -u run.py data2 findbugs | tee Data2/Data2_findbugs.log
bloxbatch -db doop/last-analysis -query RealM | sort > Data2/findbugs_M.facts
bloxbatch -db doop/last-analysis -query RealD0 | sort > Data2/findbugs_D0.facts
bloxbatch -db doop/last-analysis -query RealD2 | sort > Data2/findbugs_D2.facts
bloxbatch -db doop/last-analysis -query RealD3 | sort > Data2/findbugs_D3.facts

rm -r doop/cache/*

python -u run.py data2 jedit | tee Data2/Data2_jedit.log
bloxbatch -db doop/last-analysis -query RealM | sort > Data2/jedit_M.facts
bloxbatch -db doop/last-analysis -query RealD0 | sort > Data2/jedit_D0.facts
bloxbatch -db doop/last-analysis -query RealD2 | sort > Data2/jedit_D2.facts
bloxbatch -db doop/last-analysis -query RealD3 | sort > Data2/jedit_D3.facts

rm -r doop/cache/*

#python -u run.py data2 briss | tee Data2/Data2_briss.log
#bloxbatch -db doop/last-analysis -query RealM | sort > Data2/xalan_M.facts
#bloxbatch -db doop/last-analysis -query RealD0 | sort > Data2/xalan_D0.facts
#bloxbatch -db doop/last-analysis -query RealD2 | sort > Data2/xalan_D2.facts
#bloxbatch -db doop/last-analysis -query RealD3 | sort > Data2/xalan_D3.facts

#rm -r doop/cache/*

python -u run.py data2 fop | tee Data2/Data2_fop.log
bloxbatch -db doop/last-analysis -query RealM | sort > Data2/fop_M.facts
bloxbatch -db doop/last-analysis -query RealD0 | sort > Data2/fop_D0.facts
bloxbatch -db doop/last-analysis -query RealD2 | sort > Data2/fop_D2.facts
bloxbatch -db doop/last-analysis -query RealD3 | sort > Data2/fop_D3.facts

rm -r doop/cache/*

#python -u run.py data2 batik | tee Data2/Data2_batik.log
#bloxbatch -db doop/last-analysis -query RealM | sort > Data2/xalan_M.facts
#bloxbatch -db doop/last-analysis -query RealD0 | sort > Data2/xalan_D0.facts
#bloxbatch -db doop/last-analysis -query RealD2 | sort > Data2/xalan_D2.facts
#bloxbatch -db doop/last-analysis -query RealD3 | sort > Data2/xalan_D3.facts

#rm -r doop/cache/*

python -u run.py data2 checkstyle | tee Data2/Data2_checkstyle.log
bloxbatch -db doop/last-analysis -query RealM | sort > Data2/checkstyle_M.facts
bloxbatch -db doop/last-analysis -query RealD0 | sort > Data2/checkstyle_D0.facts
bloxbatch -db doop/last-analysis -query RealD2 | sort > Data2/checkstyle_D2.facts
bloxbatch -db doop/last-analysis -query RealD3 | sort > Data2/checkstyle_D3.facts

rm -r doop/cache/*

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




'''

python -u run.py 3obj xalan | tee 3obj/3obj_xalan.log
rm -r doop/cache/*

python -u run.py 3obj chart | tee 3obj/3obj_chart.log
rm -r doop/cache/*

python -u run.py 3obj bloat | tee 3obj/3obj_bloat.log
rm -r doop/cache/*

python -u run.py 3obj findbugs | tee 3obj/3obj_findbugs.log
rm -r doop/cache/*

python -u run.py 3obj jedit | tee 3obj/3obj_jedit.log
rm -r doop/cache/*

python -u run.py 3obj briss | tee 3obj/3obj_briss.log
rm -r doop/cache/*

python -u run.py 3obj fop | tee 3obj/3obj_fop.log
rm -r doop/cache/*

python -u run.py 3obj batik | tee 3obj/3obj_batik.log
rm -r doop/cache/*

python -u run.py 3obj checkstyle | tee 3obj/3obj_checkstyle.log
rm -r doop/cache/*

python -u run.py 3obj sunflow | tee 3obj/3obj_sunflow.log
rm -r doop/cache/*

python -u run.py 3obj jpc | tee 3obj/3obj_jpc.log
rm -r doop/cache/*


'''

