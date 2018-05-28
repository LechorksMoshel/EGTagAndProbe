# TEMPLATE used for automatic script submission of multiple datasets

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'TagAndProbe_test'
config.General.workArea = 'DefaultCrab3Area'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'reEmulL1_new.py'
config.JobType.inputFiles = ['EcalTPG_306152_moved_to_1.db']
#config.JobType.allowUndistributedCMSSW = True
config.section_("Data")
config.Data.inputDataset = '/SingleElectron/Run2017F-PromptReco-v1/MINIAOD'  #'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80-FlatPU28to62HcalNZSRAWAODSIM_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/RAWAODSIM'

########################################### Parent Dataset #######################################
config.Data.secondaryInputDataset= '/SingleElectron/Run2017F-v1/RAW'#'/SingleElectron/Run2017F-v1/RAW'
##################################################################################################

config.Data.inputDBS = 'global'
#config.Data.runRange =  '300742-301283'
config.Data.runRange =  '306460'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 15000 #number of events per jobs
config.Data.totalUnits = 2000 #number of event
config.Data.outLFNDirBase = '/store/user/syuan/TagAndProbeTrees/Emulation/callibrations/reEmulL1'  #'/store/user/tstreble/TagAndProbeTrees'
#config.Data.outLFNDirBase = '/eos/user/s/syuan/TagAndProbeTrees/Emulation/callibrations'  #'/store/user/tstreble/TagAndProbeTrees'
config.Data.publication = False
config.Data.outputDatasetTag = 'TagAndProbe_test'
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt'
# json with 3.99/fb

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.storageSite = 'T2_CH_CERN'
config.Data.ignoreLocality=True
config.Site.whitelist = ["T3_US*"]

