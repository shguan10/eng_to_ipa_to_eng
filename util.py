with open("data/eng2ipa.pk","rb") as f: eng2ipa = pk.load(f)
with open("data/ipa2eng.pk","rb") as f: ipa2eng = pk.load(f)

ipa = list(ipa2eng)
eng = list(eng2ipa)

def totalipa():
  return len(ipa2eng)

def totaleng():
  return len(eng2ipa)

def wipaind(ind):
  return ipa[ind]

def wengind(ind):
  return eng[ind]

def convert2ipa(weng,retrieve_all=False):
  ipas = eng2ipa[weng]
  if retrieve_all: return ipas
  return ipas[0]

def convert2eng(wipa,retrieve_all=False):
  engs = ipa2eng[wipa]
  if retrieve_all: return engs
  return engs[0]