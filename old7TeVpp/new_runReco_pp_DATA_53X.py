# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: step3 --data --conditions FT_R_53_LV5::All -s RAW2DIGI,RECO --scenario HeavyIons --datatier GEN-SIM-RECO --eventcontent RECODEBUG -n 100 --repacked --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
                            secondaryFileNames = cms.untracked.vstring(),
                            #fileNames = cms.untracked.vstring('/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/066/14B65DE8-9512-E111-AA9F-BCAEC53296F6.root')
                            fileNames = cms.untracked.vstring('/store/user/velicanu/rawpp/12DA0A3E-C873-E211-9A3D-003048D2BE06.root')
                            )

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.28 $'),
    annotation = cms.untracked.string('step3 nevts:100'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RECODEBUGoutput = cms.OutputModule("PoolOutputModule",
                                           splitLevel = cms.untracked.int32(0),
                                           eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
                                           outputCommands = process.RECODEBUGEventContent.outputCommands,
                                           fileName = cms.untracked.string('DATA_RECO.root'),
                                           dataset = cms.untracked.PSet(
    #filterName = cms.untracked.string('MinBiasCollEvtSel'),
    dataTier = cms.untracked.string('RECO')
    ),
                                           )

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_P_V43D::All', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.hiRecoPFJets = process.hiRecoAllPFJets
process.hiRecoJets = process.hiRecoAllJets
process.reconstruction_step = cms.Path(process.reconstructionHeavyIons)

process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECODEBUGoutput_step = cms.EndPath(process.RECODEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.RECODEBUGoutput_step)

# from Configuration.PyReleaseValidation.ConfigBuilder import MassReplaceInputTag
# MassReplaceInputTag(process)

# process.SimpleMemoryCheck=cms.Service("SimpleMemoryCheck",
#                                       oncePerEventMode=cms.untracked.bool(False))

# process.Timing=cms.Service("Timing",
#                            useJobReport = cms.untracked.bool(True)
#                            )
