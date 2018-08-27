# EGTagAndProbe
Set of tools to evaluate L1EG trigger performance on T&amp;P

Based on TauTagAndProbe package developed by L. Cadamuro & O. Davignon
Forked from https://github.com/pkontaxa/EGTagAndProbe

### Install instructions
To run on 2018 data:(this version not tested on 2017 data yet)
Follow [L1 Trigger Emulator Stage 2 Upgrade Instructions](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideL1TStage2Instructions)
Then clone the repository:
```
git clone https://github.com/siqiyyyy/EGTagAndProbe
scram b -j4
```
Now you have set up the work directory. 


### Producing TagAndProbe ntuples with unpacked L1EG (no re-emulation)
Set flag isMC and isMINIAOD according to sample in test/test.py
HLT path used specified in python/MCAnalysis_cff.py (MC) or python/tagAndProbe_cff.py (data)
Launch test.py


### Producing TagAndProbe ntuples with emulated L1EG
test/reEmulL1.py is an example of cms pset file to run re-emulation on 2018 runC data.
Here is a checklist of code you need to modify in order to run your desired process.


### Submit job on the Grid
Modify crab3_config.py: change requestName, inputDataSet, outLFNDirBase, outputDatasetTag, storageSite
```
cd CMSSW_9_4_0_pre3/src/EGTagAndProbe/EGTagAndProbe/test
source /cvmfs/cms.cern.ch/crab3/crab.sh
voms-proxy-init -voms cms
crab submit -c crab3_config.py
```

### Producing turn-on plots
Create configuration file base on test/fitter/run/stage2_turnOnEG_fitter_test.par
```
cd CMSSW_9_4_0_pre3/src/EGTagAndProbe/EGTagAndProbe/test/fitter
make clean; make
./fit.exe run/stage2_turnOnEG_fitter_test.par
```
Create plotting script based on test/fitter/results/plot_EG_example.py
```
cd results
python plot_EG_example.py
```
