from numpy import *
from collections import Counter


def read_data(file_name):
    data = []
    with open(file_name, "r") as f:
        data = array(f.read().split("\n"))
    data = array([s.split(",") for s in data if len(s) > 0])
    return data


def classify(file_name, instance):
    data = read_data(file_name)
    classes = [t[-1] for t in data]
    class_counts = dict(Counter(classes))
    classes = set(classes)
    class_probs = dict([(c,float(class_counts[c])/len(data)) for c in classes])
    classified_data = [(c, transpose([t[:len(t)-1] for t in data if t[-1] == c])) for c in classes]
    classified_counts = dict([(c[0], [dict(Counter(a)) for a in c[1]]) for c in classified_data])
    return max([(reduce(lambda x,y: x*y, [float(v.get(k,0))/class_counts[c] for k,v in zip(instance, classified_counts[c])])*class_probs[c], c) for c in classes])


if __name__ == "__main__":
    i1 = ["sunny", "cool", "high", "strong"]
    i2 = ["overcast", "mild", "normal", "weak"]
    print classify("tennis.csv", i1)
    print classify("tennis.csv", i2)
