class Pet:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        return f'{self.name} is moving...'
    
def main():
    dog = Pet('Fritz')
    print(dog.move())

if __name__ == '__main__':
    main()
  
