import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']
    login = testdata['login']
    password = testdata['password']