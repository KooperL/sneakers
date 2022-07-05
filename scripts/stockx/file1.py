#from stockxsdk import Stockx

def fakeCall(pid):
  pidLookup = {
    'test1': 'shitty vans',
  }
  lowest_price = 100
  average = 200
  return [pidLookup[pid], lowest_price, average]


def main(pid):
  getPriceFromPID = fakeCall(pid)
  return getPriceFromPID

if __name__ == '__main__':
  main('')
