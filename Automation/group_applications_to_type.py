"""
Given an input file with application and application type
Return the metrics based on application type
Input file

wikipedia, web
cnet, audio
youtube, video
cnn, web

"""

def gather_metrics(file):
    metric_map = {}
    lines = []
    with open(file, 'r') as fh:
        data = fh.read()
    lines = data.splitlines()
    print(lines)

    for line in lines:
        words = line.split(',')
        if len(words) == 2:
            if words[-1] in metric_map:
                metric_map[words[-1].lower()].append(words[0])
            else:
                metric_map[words[-1].lower()] = [words[0]]
        else:
            print("Warning: Incorrect format at line: {}".format(line))
            continue

    print(metric_map)


def main():
    file = '/Users/sumanthkakaraparthi/Documents/MacPro-2019/Documents/scripts/Automation/application_metric.txt'
    gather_metrics(file)


if __name__ == '__main__':
    main()





