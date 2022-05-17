How to get started

The script `prepareSubmission.py` sets up a couple of text files containing the paths to input files.

Create those files by calling

```
python prepareSubmission.py
```
in the command line.

The script `loopOverFiles.py` then takes a number as an argument, and uses it to decide which input text file to read. For example

```
python loopOverFiles.py 22
```

Will try to open a file called `input_list_22.txt`, add the root files that are listed there

```
/eos/user/a/aleopold/project10/data_with_jets/user.aleopold.20229250.HGTDHitAnalysis._000616.root
/eos/user/a/aleopold/project10/data_with_jets/user.aleopold.20229250.HGTDHitAnalysis._000617.root
/eos/user/a/aleopold/project10/data_with_jets/user.aleopold.20229250.HGTDHitAnalysis._000618.root
/eos/user/a/aleopold/project10/data_with_jets/user.aleopold.20229250.HGTDHitAnalysis._000619.root
/eos/user/a/aleopold/project10/data_with_jets/user.aleopold.20229250.HGTDHitAnalysis._000620.root
/eos/user/a/aleopold/project10/data_with_jets/user.aleopold.20229250.HGTDHitAnalysis._000622.root
/eos/user/a/aleopold/project10/data_with_jets/user.aleopold.20229250.HGTDHitAnalysis._000623.root
/eos/user/a/aleopold/project10/data_with_jets/user.aleopold.20229250.HGTDHitAnalysis._000624.root
/eos/user/a/aleopold/project10/data_with_jets/user.aleopold.20229250.HGTDHitAnalysis._000626.root
/eos/user/a/aleopold/project10/data_with_jets/user.aleopold.20229250.HGTDHitAnalysis._000627.root
/eos/user/a/aleopold/project10/data_with_jets/user.aleopold.20229250.HGTDHitAnalysis._000628.root
/eos/user/a/aleopold/project10/data_with_jets/user.aleopold.20229250.HGTDHitAnalysis._000629.root
/eos/user/a/aleopold/project10/data_with_jets/user.aleopold.20229250.HGTDHitAnalysis._000630.root
...
```

to a `TChain` and then loop over them. The `loopOverFiles.py` script then produces an output called `output_file_22.root` (same numbering), including the defined histograms.

After all files have run, they can be merged using e.g.

```
hadd -f output.root output_file_*.root
```
