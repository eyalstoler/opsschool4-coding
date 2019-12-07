import json

def parse_json(json_file):
    with open(json_file, 'r') as json_data:
        return json.load(json_data)

def bucket_parser(json_input):
    yaml_file = 'output.yaml'
    treshold = json_input['buckets']
    treshold.extend([0,100])
    treshold.sort(reverse=True)
    ppl_ages = json_input['ppl_ages'].items()

    while len(treshold) > 1:
        min_range = treshold.pop()
        max_range = treshold[-1]
        sort_and_append(min_range, max_range, ppl_ages, yaml_file)

def sort_and_append(min, max, tuples, output_file):
    ppl = []
    for person, age in tuples:
        if (min <= age < max):
            ppl.append(person)

    with open(output_file, 'a') as output:
        if ppl:
            output.write(str(min) + '-' + str(max) + ':\n    -' + '\n    -'.join(ppl) + '\n')

def main():
    json_input = parse_json('hw.json')
    bucket_parser(json_input)

if __name__ == '__main__':
    main()
