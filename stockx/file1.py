#from stockxsdk import Stockx

def fakeCall(pid):
  lowest_price = 100
  average = 200
  return [pid, lowest_price, average]


def main(pid):
  getPriceFromPID = fakeCall(pid)
  return getPriceFromPID

if __name__ == '__main__':
  main('BB1234')
