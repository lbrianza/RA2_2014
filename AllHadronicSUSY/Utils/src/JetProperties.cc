// -*- C++ -*-
//
// Package:    JetProperties
// Class:      JetProperties
// 
/**\class JetProperties JetProperties.cc RA2Classic/JetProperties/src/JetProperties.cc
 * 
 * Description: [one line class summary]
 * 
 * Implementation:
 *     [Notes on implementation]
 */
//
// Original Author:  Arne-Rasmus Draeger,68/111,4719,
//         Created:  Fri Apr 11 16:35:33 CEST 2014
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Candidate/interface/Candidate.h"

#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrectorCalculator.h"
//
// class declaration
//

class JetProperties : public edm::EDProducer {
public:
	explicit JetProperties(const edm::ParameterSet&);
	~JetProperties();
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
	virtual void beginJob() ;
	virtual void produce(edm::Event&, const edm::EventSetup&);
	virtual void endJob() ;
	
	virtual void beginRun(edm::Run&, edm::EventSetup const&);
	virtual void endRun(edm::Run&, edm::EventSetup const&);
	virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
	virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
	edm::InputTag JetTag_;
  edm::InputTag RhoTag_;
  std::vector<std::string> jecPayloadNames_;
  //	std::string   btagname_;

	
	
	// ----------member data ---------------------------
};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
JetProperties::JetProperties(const edm::ParameterSet& iConfig):
  jecPayloadNames_( iConfig.getParameter<std::vector<std::string> >("jecPayloadNames") ) // JEC level payloads   
{
	JetTag_ = iConfig.getParameter<edm::InputTag>("JetTag");
	RhoTag_ = iConfig.getParameter<edm::InputTag>("RhoTag");

	//	btagname_ = iConfig.getParameter<std::string>  ("BTagInputTag");
	//register your products
	/* Examples
	 *   produces<ExampleData2>();
	 * 
	 *   //if do put with a label
	 *   produces<ExampleData2>("label");
	 * 
	 *   //if you want to put into the Run
	 *   produces<ExampleData2,InRun>();
	 */
	//now do what ever other initialization is needed
	//register your products
	produces<std::vector<pat::Jet> >();
	const std::string string0("jetArea");
	produces<std::vector<double> > (string0).setBranchAlias(string0);
	const std::string string1("chargedHadronEnergyFraction");
	produces<std::vector<double> > (string1).setBranchAlias(string1);
	const std::string string2("chargedHadronMultiplicity");
	produces<std::vector<int> > (string2).setBranchAlias(string2);
	const std::string string3("neutralHadronEnergyFraction");
	produces<std::vector<double> > (string3).setBranchAlias(string3);
	const std::string string4("neutralHadronMultiplicity");
	produces<std::vector<int> > (string4).setBranchAlias(string4);
	const std::string string5("chargedEmEnergyFraction");
	produces<std::vector<double> > (string5).setBranchAlias(string5);
	const std::string string6("neutralEmEnergyFraction");
	produces<std::vector<double> > (string6).setBranchAlias(string6);
// 	const std::string string7("patJetsNeutralEmFractionPBNR");
// 	produces<std::vector<double> > (string7).setBranchAlias(string7);
	const std::string string8("electronMultiplicity");
	produces<std::vector<int> > (string8).setBranchAlias(string8);
	const std::string string9("photonEnergyFraction");
	produces<std::vector<double> > (string9).setBranchAlias(string9);
	const std::string string10("photonMultiplicity");
	produces<std::vector<int> > (string10).setBranchAlias(string10);
	const std::string string11("muonEnergyFraction");
	produces<std::vector<double> > (string11).setBranchAlias(string11);
	const std::string string12("muonMultiplicity");
	produces<std::vector<int> > (string12).setBranchAlias(string12);
	const std::string string13("bDiscriminatorCSV");
	produces<std::vector<double> > (string13).setBranchAlias(string13);
	const std::string string14("isLooseJetId");
	produces<std::vector<bool> > (string14).setBranchAlias(string14);
	const std::string string15("bDiscriminatorICSV");
	produces<std::vector<double> > (string15).setBranchAlias(string15);
        const std::string string24("PtCorr");
        produces<std::vector<double> > (string24).setBranchAlias(string24);
        const std::string string25("EtaCorr");
        produces<std::vector<double> > (string25).setBranchAlias(string25);
        const std::string string26("PhiCorr");
        produces<std::vector<double> > (string26).setBranchAlias(string26);
        const std::string string27("ECorr");
        produces<std::vector<double> > (string27).setBranchAlias(string27);	
}


JetProperties::~JetProperties()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
JetProperties::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	using namespace edm;
	std::auto_ptr<std::vector<pat::Jet> > prodJets(new std::vector<pat::Jet>());
	
	std::auto_ptr< std::vector<double> > jetArea(new std::vector<double>);
	std::auto_ptr< std::vector<double> > chargedHadronEnergyFraction(new std::vector<double>);
	std::auto_ptr< std::vector<int> > chargedHadronMultiplicity(new std::vector<int>);
	std::auto_ptr< std::vector<double> > neutralHadronEnergyFraction(new std::vector<double>);
	std::auto_ptr< std::vector<int> > neutralHadronMultiplicity(new std::vector<int>);
	std::auto_ptr< std::vector<double> > chargedEmEnergyFraction(new std::vector<double>);
	std::auto_ptr< std::vector<double> > neutralEmEnergyFraction(new std::vector<double>);
// 	std::auto_ptr< std::vector<double> > patJetsNeutralEmFractionPBNR(new std::vector<double>);
	std::auto_ptr< std::vector<double> > electronEnergyFraction(new std::vector<double>);
	std::auto_ptr< std::vector<int> > electronMultiplicity(new std::vector<int>);
	std::auto_ptr< std::vector<double> > photonEnergyFraction(new std::vector<double>);
	std::auto_ptr< std::vector<int> > photonMultiplicity(new std::vector<int>);
	std::auto_ptr< std::vector<double> > muonEnergyFraction(new std::vector<double>);
	std::auto_ptr< std::vector<int> > muonMultiplicity(new std::vector<int>);
	std::auto_ptr< std::vector<double> > bDiscriminatorCSV(new std::vector<double>);
	std::auto_ptr< std::vector<bool> > isLooseJetId(new std::vector<bool>);
	std::auto_ptr< std::vector<double> > bDiscriminatorICSV(new std::vector<double>);
	std::auto_ptr< std::vector<double> > PtCorr(new std::vector<double>);
	std::auto_ptr< std::vector<double> > EtaCorr(new std::vector<double>);
	std::auto_ptr< std::vector<double> > PhiCorr(new std::vector<double>);
	std::auto_ptr< std::vector<double> > ECorr(new std::vector<double>);
	using namespace edm;
	using namespace reco;
	using namespace pat;
	edm::Handle< edm::View<pat::Jet> > Jets;
	iEvent.getByLabel(JetTag_,Jets);
	edm::Handle<double> rho_ ;
        iEvent.getByLabel(RhoTag_, rho_);

	//  Load the JetCorrectorParameter objects into a vector, IMPORTANT: THE ORDER MATTERS HERE !!!! 
	std::vector<JetCorrectorParameters> vPar;
	for ( std::vector<std::string>::const_iterator payloadBegin = jecPayloadNames_.begin(),
		payloadEnd = jecPayloadNames_.end(), ipayload = payloadBegin; ipayload != payloadEnd; ++ipayload ) {
	  JetCorrectorParameters pars(*ipayload);
	  vPar.push_back(pars);
	}

	FactorizedJetCorrector *JetCorrector = new FactorizedJetCorrector(vPar);

	if( Jets.isValid() ) {
	  edm::View<pat::Jet>::const_iterator ijet = Jets->begin();
		for(unsigned int i=0; i<Jets->size();i++)
		{
		  bool looseJetId=false;

		  reco::Candidate::LorentzVector uncorrJet;
		  // The pat::Jet "knows" if it has been corrected, so here
		  // we can "uncorrect" the entire jet to apply the corrections
		  // we want here.
		  pat::Jet const * pJet = dynamic_cast<pat::Jet const *>( &*ijet );
		  if ( pJet != 0 ) {
		    uncorrJet = pJet->correctedP4(0);
		  }
		  // Otherwise, if we do not have pat::Jets on input, we just assume
		  // the user has not corrected them upstream and use it as raw.
		  else {
		    uncorrJet = ijet->p4();
		  }

		  JetCorrector->setJetEta(uncorrJet.eta());
		  JetCorrector->setJetPt(uncorrJet.pt());
		  JetCorrector->setJetA(ijet->jetArea());
		  JetCorrector->setRho(*(rho_.product())); 

		  double correction = JetCorrector->getCorrection();
		  ijet++;

			prodJets->push_back(pat::Jet(Jets->at(i)));
			PtCorr->push_back(correction*uncorrJet.pt());
			EtaCorr->push_back(correction*uncorrJet.eta());
			PhiCorr->push_back(correction*uncorrJet.phi());
			ECorr->push_back(correction*uncorrJet.e());
			jetArea->push_back( Jets->at(i).jetArea() );
			chargedHadronEnergyFraction->push_back( Jets->at(i).chargedHadronEnergyFraction() );
			chargedHadronMultiplicity->push_back( Jets->at(i).chargedHadronMultiplicity() );
			neutralHadronEnergyFraction->push_back( Jets->at(i).neutralHadronEnergyFraction() );
			neutralHadronMultiplicity->push_back( Jets->at(i).neutralHadronMultiplicity() );
			chargedEmEnergyFraction->push_back( Jets->at(i).chargedEmEnergyFraction() );
			neutralEmEnergyFraction->push_back( Jets->at(i).neutralEmEnergyFraction() );
// 			patJetsNeutralEmFractionPBNR->push_back( Jets->at(i).patJetsNeutralEmFractionPBNR() / Jets->at(i).jecFactor(0) );
			electronEnergyFraction->push_back( Jets->at(i).electronEnergyFraction() );
			electronMultiplicity->push_back( Jets->at(i).electronMultiplicity() );
			photonEnergyFraction->push_back( Jets->at(i).photonEnergyFraction() );
			photonMultiplicity->push_back( Jets->at(i).photonMultiplicity() );
			muonEnergyFraction->push_back( Jets->at(i).muonEnergyFraction() );
			muonMultiplicity->push_back( Jets->at(i).muonMultiplicity() );
			bDiscriminatorCSV->push_back( Jets->at(i).bDiscriminator("combinedSecondaryVertexBJetTags") );
			bDiscriminatorICSV->push_back( Jets->at(i).bDiscriminator("combinedInclusiveSecondaryVertexV2BJetTags") );

			if (Jets->at(i).nConstituents() > 1 &&
                            Jets->at(i).photonEnergyFraction() < 0.99 &&
                            Jets->at(i).neutralHadronEnergyFraction() < 0.99 &&
                            Jets->at(i).muonEnergyFraction() < 0.8 &&
                            Jets->at(i).electronEnergyFraction() < 0.9 &&
                            (Jets->at(i).chargedHadronMultiplicity() > 0 || fabs(Jets->at(i).eta())>2.4 ) &&
			    (Jets->at(i).chargedEmEnergyFraction() < 0.99 || fabs(Jets->at(i).eta())>2.4 ) &&
                            (Jets->at(i).chargedHadronEnergyFraction() > 0. || fabs(Jets->at(i).eta())>2.4 ) )
                          looseJetId = true;
                        isLooseJetId->push_back(looseJetId);
		}
	}
	delete JetCorrector;

	const std::string string00("");
	iEvent.put(prodJets );
	
	const std::string string0("jetArea");
	iEvent.put(jetArea,string0);
	const std::string string1("chargedHadronEnergyFraction");
	iEvent.put(chargedHadronEnergyFraction,string1);
	const std::string string2("chargedHadronMultiplicity");
	iEvent.put(chargedHadronMultiplicity,string2);
	const std::string string3("neutralHadronEnergyFraction");
	iEvent.put(neutralHadronEnergyFraction,string3);
	const std::string string4("neutralHadronMultiplicity");
	iEvent.put(neutralHadronMultiplicity,string4);
	const std::string string5("chargedEmEnergyFraction");
	iEvent.put(chargedEmEnergyFraction,string5);
	const std::string string6("neutralEmEnergyFraction");
	iEvent.put(neutralEmEnergyFraction,string6);
// 	const std::string string7("patJetsNeutralEmFractionPBNR");
// 	iEvent.put(patJetsNeutralEmFractionPBNR,string7);
	const std::string string8("electronMultiplicity");
	iEvent.put(electronMultiplicity,string8);
	const std::string string9("photonEnergyFraction");
	iEvent.put(photonEnergyFraction,string9);
	const std::string string10("photonMultiplicity");
	iEvent.put(photonMultiplicity,string10);
	const std::string string11("muonEnergyFraction");
	iEvent.put(muonEnergyFraction,string11);
	const std::string string12("muonMultiplicity");
	iEvent.put(muonMultiplicity,string12);
	const std::string string13("bDiscriminatorCSV");
	iEvent.put(bDiscriminatorCSV,string13);
	const std::string string14("isLooseJetId");
	iEvent.put(isLooseJetId,string14);
	const std::string string15("bDiscriminatorICSV");
	iEvent.put(bDiscriminatorICSV,string15);
	const std::string string24("PtCorr");
	iEvent.put(PtCorr,string24);
	const std::string string25("EtaCorr");
	iEvent.put(EtaCorr,string25);
	const std::string string26("PhiCorr");
	iEvent.put(PhiCorr,string26);
	const std::string string27("ECorr");
	iEvent.put(ECorr,string27);
		
}

// ------------ method called once each job just before starting event loop  ------------
void 
JetProperties::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
JetProperties::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
JetProperties::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
JetProperties::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
JetProperties::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
JetProperties::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
JetProperties::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetProperties);
