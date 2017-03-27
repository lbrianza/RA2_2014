from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'data_mu'
config.General.workArea = 'data_mu'
config.section_('JobType')
config.JobType.psetName = 'TreeMaker/test/runMakeTreeFromMiniAOD_cfg.py'
config.JobType.pluginName = 'Analysis'
config.JobType.pyCfgParams = ['global_tag=80X_dataRun2_v6','leptonFilter=True', 'MC=False', 'isCrab=True', 'DoJECCorrection=True', 'DoPuppi=True','ReDoPruningAndSoftdropPuppi=True']
config.JobType.allowUndistributedCMSSW = True
#config.JobType.maxMemoryMB = 2500    # 2.5 GB                      
config.JobType.maxJobRuntimeMin = 900 #15 h
config.JobType.inputFiles = ['Summer15_25nsV6_DATA_L1FastJet_AK8PFchs.txt','Summer15_25nsV6_DATA_L2Relative_AK8PFchs.txt','Summer15_25nsV6_DATA_L3Absolute_AK8PFchs.txt','Summer15_25nsV6_DATA_L2L3Residual_AK8PFchs.txt','Summer15_25nsV6_DATA_L1FastJet_AK4PFchs.txt','Summer15_25nsV6_DATA_L2Relative_AK4PFchs.txt','Summer15_25nsV6_DATA_L3Absolute_AK4PFchs.txt','Summer15_25nsV6_DATA_L2L3Residual_AK4PFchs.txt','Summer15_25nsV6_DATA_Uncertainty_AK4PFchs.txt','Summer15_25nsV6_DATA_Uncertainty_AK8PFchs.txt','Summer15_25nsV6_DATA_L1FastJet_AK8PFPuppi.txt','Summer15_25nsV6_DATA_L2Relative_AK8PFPuppi.txt','Summer15_25nsV6_DATA_L3Absolute_AK8PFPuppi.txt','Summer15_25nsV6_DATA_L2L3Residual_AK8PFPuppi.txt','Summer15_25nsV6_DATA_L1FastJet_AK4PFPuppi.txt','Summer15_25nsV6_DATA_L2Relative_AK4PFPuppi.txt','Summer15_25nsV6_DATA_L3Absolute_AK4PFPuppi.txt','Summer15_25nsV6_DATA_L2L3Residual_AK4PFPuppi.txt','Summer15_25nsV6_DATA_Uncertainty_AK4PFPuppi.txt','Summer15_25nsV6_DATA_Uncertainty_AK8PFPuppi.txt' ] #TO BE UPDATED
config.section_('Data')
config.Data.inputDataset = '/SingleMuon/Run2016B-PromptReco-v1/MINIAOD'
config.Data.unitsPerJob = 10
#config.Data.lumiMask = 'json/Cert_246908-259891_13TeV_PromptReco_Collisions15_25ns_JSON.txt' #last version (1.56/fb)
#config.Data.lumiMask = 'json/Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt' #for the AN (1.26/fb)
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt' #final SILVER (2.5/fb)
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Reprocessing/Cert_13TeV_16Dec2016ReReco_Collisions15_25ns_JSON_v2.txt' #final GOLDEN (2.1/fb)
#config.Data.lumiMask = 'json/Cert_246908-259891_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt' # 1.9/fb
config.Data.inputDBS = 'global' #'http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet'
config.Data.splitting = 'LumiBased'
config.Data.outLFNDirBase = '/store/group/dpg_ecal/alca_ecalcalib/ecalMIBI/lbrianza/ntuple_data_mu/'
config.section_('User')
config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
config.Site.blacklist= ['T2_US_Purdue','T2_UA_KIPT']

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand

    #Make sure you set this parameter (here or above in the config it does not matter)
    config.General.workArea = 'data_24may2016_v1'

    def submit(config):
        res = crabCommand('submit', config = config)

    #########    From now on that's what users should modify: this is the a-la-CRAB2 configuration part.
        
    config.General.requestName = 'data_mu_16dec_25ns_runD'
    config.Data.inputDataset = '/SingleMuon/Run2016B-PromptReco-v2/MINIAOD'
    config.Data.outLFNDirBase = '/store/group/dpg_ecal/alca_ecalcalib/ecalMIBI/lbrianza/data_24may2016_v1/data_mu_16dec_25ns_runD/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()
    
    config.General.requestName = 'data_el_16dec_25ns_runD'
    config.Data.inputDataset = '/SingleElectron/Run2016B-PromptReco-v2/MINIAOD'
    config.Data.outLFNDirBase = '/store/group/dpg_ecal/alca_ecalcalib/ecalMIBI/lbrianza/data_24may2016_v1/data_el_16dec_25ns_runD/'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    #...
