from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'data_mu'
config.General.workArea = 'data_mu'
config.section_('JobType')
config.JobType.psetName = 'TreeMaker/test/runMakeTreeFromMiniAOD_cfg.py'
config.JobType.pluginName = 'Analysis'
config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True']
config.JobType.allowUndistributedCMSSW = True
#config.JobType.maxMemoryMB = 2500    # 2.5 GB                      
config.JobType.maxJobRuntimeMin = 900 #15 h
config.JobType.inputFiles = ['Spring16_23Sep2016HV2_DATA_L1FastJet_AK8PFchs.txt','Spring16_23Sep2016HV2_DATA_L2Relative_AK8PFchs.txt','Spring16_23Sep2016HV2_DATA_L3Absolute_AK8PFchs.txt','Spring16_23Sep2016HV2_DATA_L2L3Residual_AK8PFchs.txt','Spring16_23Sep2016HV2_DATA_L1FastJet_AK4PFchs.txt','Spring16_23Sep2016HV2_DATA_L2Relative_AK4PFchs.txt','Spring16_23Sep2016HV2_DATA_L3Absolute_AK4PFchs.txt','Spring16_23Sep2016HV2_DATA_L2L3Residual_AK4PFchs.txt','Spring16_23Sep2016HV2_DATA_Uncertainty_AK4PFchs.txt','Spring16_23Sep2016HV2_DATA_Uncertainty_AK8PFchs.txt','Spring16_23Sep2016HV2_DATA_L1FastJet_AK8PFPuppi.txt','Spring16_23Sep2016HV2_DATA_L2Relative_AK8PFPuppi.txt','Spring16_23Sep2016HV2_DATA_L3Absolute_AK8PFPuppi.txt','Spring16_23Sep2016HV2_DATA_L2L3Residual_AK8PFPuppi.txt','Spring16_23Sep2016HV2_DATA_L1FastJet_AK4PFPuppi.txt','Spring16_23Sep2016HV2_DATA_L2Relative_AK4PFPuppi.txt','Spring16_23Sep2016HV2_DATA_L3Absolute_AK4PFPuppi.txt','Spring16_23Sep2016HV2_DATA_L2L3Residual_AK4PFPuppi.txt','Spring16_23Sep2016HV2_DATA_Uncertainty_AK4PFPuppi.txt','Spring16_23Sep2016HV2_DATA_Uncertainty_AK8PFPuppi.txt' ]
config.section_('Data')
config.Data.inputDataset = '/SingleMuon/Run2015B-PromptReco-v1/MINIAOD'
config.Data.unitsPerJob = 7
config.Data.lumiMask = 'json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt' #Moriond17: 36.814pb-1
config.Data.inputDBS = 'global' #'http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet'
config.Data.splitting = 'LumiBased'
config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/'
#config.Data.runRange = '275126-275783'
config.section_('User')
config.section_('Site')
config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.blacklist= ['T2_US_Purdue','T2_UA_KIPT']

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand

    #Make sure you set this parameter (here or above in the config it does not matter)
    config.General.workArea = 'Crab_data_23Sep2016'

    def submit(config):
        res = crabCommand('submit', config = config)

    #########    From now on that's what users should modify: this is the a-la-CRAB2 configuration part.
    config.General.requestName = 'data_el_2016_runB_v2'
    config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True', 'IsRun2016BCD=True']
    config.Data.inputDataset = '/SingleElectron/Run2016B-23Sep2016-v2/MINIAOD'
    config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/Jan102016/data_el_2016_runB_v2/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'data_el_2016_runB_v3'
    config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True', 'IsRun2016BCD=True']
    config.Data.inputDataset = '/SingleElectron/Run2016B-23Sep2016-v3/MINIAOD'
    config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/Jan102016/data_el_2016_runB_v3/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'data_el_2016_runC_v1'
    config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True', 'IsRun2016BCD=True']
    config.Data.inputDataset = '/SingleElectron/Run2016C-23Sep2016-v1/MINIAOD'
    config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/Jan102016/data_el_2016_runC_v1/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'data_el_2016_runD_v1'
    config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True', 'IsRun2016BCD=True']
    config.Data.inputDataset = '/SingleElectron/Run2016D-23Sep2016-v1/MINIAOD'
    config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/Jan102016/data_el_2016_runD_v1/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'data_el_2016_runE_v1'
    config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True', 'IsRun2016EF=True']
    config.Data.inputDataset = '/SingleElectron/Run2016E-23Sep2016-v1/MINIAOD'
    config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/Jan102016/data_el_2016_runE_v1/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'data_el_2016_runF_v1'
    config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True', 'IsRun2016EF=True']
    config.Data.inputDataset = '/SingleElectron/Run2016F-23Sep2016-v1/MINIAOD'
    config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/Jan102016/data_el_2016_runF_v1/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'data_el_2016_runG_v1'
    config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True', 'IsRun2016G=True']
    config.Data.inputDataset = '/SingleElectron/Run2016G-23Sep2016-v1/MINIAOD'
    config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/Jan102016/data_el_2016_runG_v1/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'data_el_2016_runH_v1'
    config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True', 'IsRun2016H=True']
    config.Data.inputDataset = '/SingleElectron/Run2016G-23Sep2016-v1/MINIAOD'
    config.Data.inputDataset = '/SingleElectron/Run2016H-PromptReco-v1/MINIAOD'
    config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/Jan102016/data_el_2016_runH_v1/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'data_el_2016_runH_v2'
    config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True', 'IsRun2016H=True']
    config.Data.inputDataset = '/SingleElectron/Run2016H-PromptReco-v2/MINIAOD'
    config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/Jan102016/data_el_2016_runH_v2/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'data_el_2016_runH_v3'
    config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True', 'IsRun2016H=True']
    config.Data.inputDataset = '/SingleElectron/Run2016H-PromptReco-v3/MINIAOD'
    config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/Jan102016/data_el_2016_runH_v3/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'data_mu_2016_runB_v3'
    config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True', 'IsRun2016BCD=True']
    config.Data.inputDataset = '/SingleMuon/Run2016B-23Sep2016-v3/MINIAOD'
    config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/Jan102016/data_mu_2016_runB_v3/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'data_mu_2016_runC_v1'
    config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True', 'IsRun2016BCD=True']
    config.Data.inputDataset = '/SingleMuon/Run2016C-23Sep2016-v1/MINIAOD'
    config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/Jan102016/data_mu_2016_runC_v1/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'data_mu_2016_runD_v1'
    config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True', 'IsRun2016BCD=True']
    config.Data.inputDataset = '/SingleMuon/Run2016D-23Sep2016-v1/MINIAOD'
    config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/Jan102016/data_mu_2016_runD_v1/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'data_mu_2016_runE_v1'
    config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True', 'IsRun2016EF=True']
    config.Data.inputDataset = '/SingleMuon/Run2016E-23Sep2016-v1/MINIAOD'
    config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/Jan102016/data_mu_2016_runE_v1/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'data_mu_2016_runF_v1'
    config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True', 'IsRun2016EF=True']
    config.Data.inputDataset = '/SingleMuon/Run2016F-23Sep2016-v1/MINIAOD'
    config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/Jan102016/data_mu_2016_runF_v1/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'data_mu_2016_runG_v1'
    config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True', 'IsRun2016G=True']
    config.Data.inputDataset = '/SingleMuon/Run2016G-23Sep2016-v1/MINIAOD'
    config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/Jan102016/data_mu_2016_runG_v1/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'data_mu_2016_runH_v1'
    config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True', 'IsRun2016H=True']
    config.Data.inputDataset = '/SingleMuon/Run2016H-PromptReco-v1/MINIAOD'
    config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/Jan102016/data_mu_2016_runH_v1/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'data_mu_2016_runH_v2'
    config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True', 'IsRun2016H=True']
    config.Data.inputDataset = '/SingleMuon/Run2016H-PromptReco-v2/MINIAOD'
    config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/Jan102016/data_mu_2016_runH_v2/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'data_mu_2016_runH_v3'
    config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_2016SeptRepro_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True',  'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True', 'IsRun2016H=True']
    config.Data.inputDataset = '/SingleMuon/Run2016H-PromptReco-v3/MINIAOD'
    config.Data.outLFNDirBase = '/store/user/rasharma/aQGC_Ntuples/FirstStepOutput/Jan102016/data_mu_2016_runH_v3/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    #...
