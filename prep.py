import json
import eng_to_ipa as ipa
import pickle as pk
from tqdm import tqdm
def prep():
  with open("data/english-words/words_dictionary.json") as f:
    d = f.read()
  engwords = json.loads(d)
  engwords = list(engwords)
  eng2ipa = dict()
  ipa2eng = dict()

  total = len(engwords)

  for i in tqdm(range(total)):
    w = engwords[i]
    if not ipa.isin_cmu(w): continue
    wipas = ipa.convert(w,retrieve_all=True)

    eng2ipa[w] = wipas

    for wipa in wipas:
      if wipa not in ipa2eng: ipa2eng[wipa] = [w]
      else:
        ipa2eng[wipa].append(w)

  # now save eng2ipa and ipa2eng to a pickle
  with open("data/eng2ipa.pk","wb") as f:
    pk.dump(eng2ipa,f)
  with open("data/ipa2eng.pk","wb") as f:
    pk.dump(ipa2eng,f)


if __name__ == '__main__':
  prep()