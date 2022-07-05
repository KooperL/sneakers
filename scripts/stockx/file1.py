def fakeCall(pid):
  pidLookup = {
    '0001': {
      'name': 'Vans',
      'condition': 'Brand new',
      'lowestOffer': '200',
      'averageOffer': '450'
    },
    '0002': {
      'name': 'Air force 1\'s',
      'condition': 'Mild',
      'lowestOffer': '15',
      'averageOffer': '23'
    },
  }
  return pidLookup[pid]


def main(pid):
  getPriceFromPID = fakeCall(pid)
  # This is where you'd normally call an API 
  print(getPriceFromPID)
  return getPriceFromPID

if __name__ == '__main__':
  main('0001')
