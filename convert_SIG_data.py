import sys


def convert(infile, outfile1, outfile2):
  out_src = open(outfile1, 'w')
  out_trg = open(outfile2, 'w')
  for line in open(infile):
    lemma, tag, form = line.strip().split('\t')
    lemma = u' '.join(list(lemma))
    form = u' '.join(list(form))
    tag = u' '.join(tag.split(','))
    out_src.write(tag + ' ' + lemma + '\n')
    out_trg.write(form + '\n')
   


if __name__ == '__main__':
  infile = sys.argv[1]
  outfile1 = sys.argv[2]
  outfile2 = sys.argv[3]
  convert(infile, outfile1, outfile2)
