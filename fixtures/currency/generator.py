import json

def generate_fixture(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    currencies = data['data']
    
    fixtures = []
    for code, currency_data in currencies.items():
        fixture = {
            'model': 'convertor.currency',
            'pk': len(fixtures) + 1,
            'fields': {
                'code': currency_data['code'],
                'rate': currency_data['value']
            }
        }
        fixtures.append(fixture)
    
    with open(output_file, 'w') as f:
        json.dump(fixtures, f, indent=4)

if __name__ == '__main__':
    input_file = 'data.json'
    output_file = 'currency_fixture.json'
    generate_fixture(input_file, output_file)
    print(f'Fixture generated: {output_file}')
