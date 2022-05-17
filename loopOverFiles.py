import ROOT
import os
import argparse

def createPtHisto(infiles, outfile):
    # in_file = ROOT.TFile.Open(infile, 'READ')
    # tree = in_file.Get("Data")

    chain = ROOT.TChain("Data")
    for line in file(infiles):
        print "Adding file: " + line
        chain.AddFile(line.strip())

    m_jet_pt = ROOT.vector('double')()
    chain.SetBranchAddress("m_jet_pt", m_jet_pt)

    hist_jet_pt = ROOT.TH1F("hist_jet_pt", ";p_{T}^{jet} [GeV]", 100, 0, 2000)

    for i in range(chain.GetEntries()):
        if i%1000 == 0:
            print("processed", i, "events")
        chain.GetEntry(i)
        for pt in m_jet_pt:
            hist_jet_pt.Fill(pt/1.e3) ##from MeV to GeV

    output_file = ROOT.TFile.Open(outfile, 'RECREATE')
    output_file.cd()

    hist_jet_pt.Write()

    output_file.Close()
    # in_file.Close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="name of the input file")
    args = parser.parse_args()

    # path = '/eos/user/a/aleopold/project10/data_with_jets'
    # createPtHisto(os.path.join(path, 'user.aleopold.20229250.HGTDHitAnalysis._001361.root'), 'output._001361.root')

    inputfile = 'input_list_{nr}.txt'.format(nr=args.input)
    outputfile = 'output_file_{nr}.root'.format(nr=args.input)

    createPtHisto(inputfile, outputfile)

if __name__ == '__main__':
    main()
