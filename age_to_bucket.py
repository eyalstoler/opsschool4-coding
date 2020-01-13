'''
This code recieves a json file which contains names paired with their ages, and the bucket ranges. 
The output is a yaml file that parses the people to buckets according to their age range.
To run this code for the sake of the test, kindly replace the json file path in the main function.
'''

import json

# Load the json file to use its information
def parse_json(json_file):
    with open(json_file, 'r') as json_data:
        return json.load(json_data)

# Create bucktet ranges, create yaml file, call sort_and_append function    
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

# Parse people into buckets and append to yaml
def sort_and_append(min, max, tuples, output_file):
    ppl = []
    for person, age in tuples:
        if (min <= age < max):
            ppl.append(person)

    with open(output_file, 'a') as output:
        if ppl:
            output.write(str(min) + '-' + str(max) + ':\n    -' + '\n    -'.join(ppl) + '\n')
            
# Please replace 'hw.json' with your json path
def main():
    json_input = parse_json('hw.json')
    bucket_parser(json_input)

if __name__ == '__main__':
    main()
