RA2_2014
========

To get framework:

	cmsrel CMSSW_8_0_11
	cd CMSSW_8_0_11/src
	cmsenv
	git cms-init
	git cms-merge-topic -u cms-met:CMSSW_8_0_X-METFilterUpdate
	git clone git@github.com:ram1123/RA2_2014.git AllHadronicSUSY 
	cd AllHadronicSUSY/
	git checkout 80x_devel
	cd ..
	git clone -b Analysis74X git@github.com:cms-edbr/ExoDiBosonResonancesRun2.git ExoDiBosonResonances
	scram b -j8
	cd AllHadronicSUSY/

To run:

	cmsRun TreeMaker/test/runMakeTreeFromMiniAOD_cfg.py global_tag=80X_mcRun2_asymptotic_2016_TrancheIV_v7 MC=True debug=False NumProcessedEvt=100 leptonFilter=True DoJECCorrection=True DoPuppi=True ReDoPruningAndSoftdropPuppi=True dataset=/store/mc/RunIISummer16MiniAODv2/WWJJToLNuQQ_LL_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DC0A604C-10C9-E611-BC55-0242AC130004.root

To Check Lumi:

	./LumiCheck.sh /json/file/name/with/path


