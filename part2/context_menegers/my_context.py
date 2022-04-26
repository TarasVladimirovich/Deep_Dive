class Resource:
    def __init__(self, name):
        self.name = name
        self.state = None


class ResourceManager:
    def __init__(self, name):
        print('* Init running *')
        self.name = name
        self.resource = None

    def __enter__(self):
        print('Entering context...')
        self.resource = Resource(self.name)
        self.resource.state = 'created'
        return self.resource

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('Exiting context...')
        self.resource.state = 'destroyed'
        if exc_type:
            print(f'*** Error occurred: {exc_type}, {exc_value} ***')
        return True  # False will raise exception higher


# Everything in global scope
with ResourceManager('Ananas') as obj:
    print('Inside with block')
    print(f'{obj.name} = {obj.state}')

print('Out of Context')
print(f'{obj.name} = {obj.state}')
print('obj' in globals())
