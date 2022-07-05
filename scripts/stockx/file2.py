def fakeCall():
  popularProducts = [
    {
      'pid': '0001',
      'manufacturer': 'Vans',
      'name': 'Olds skools',
      #'imageLocation': "{{ url_for('static', filename='images/0001.jpg') }}",
      'imageLocation': '/static/images/0001.jpg',
      'popularity': '5',
    },
    {
      'pid': '0002',
      'manufacturer': 'Nike',
      'name': 'Air force 1\'s',
      #'imageLocation': "{{ url_for('static', filename='images/0002.jpg') }}",
      'imageLocation': '/static/images/0002.jpg',
      'popularity': '5',
    },
  ]
  return popularProducts

def main():
  getPopularProducts = fakeCall()
  # This is where you'd normally call an API 
  return getPopularProducts

if __name__ == '__main__':
  main()
