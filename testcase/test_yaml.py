import yaml


def test_yaml():
    with open("../pages/main.yaml") as f:
        steps = yaml.safe_load(f)
    for step in steps:
        if "action" in step.keys():
            action = step["action"]
            if "click" == action:
                print("find(xxx).click()")


def test_replace():
    a = {"stock_name": "alibaba","xxx": '1234'}
    b = 'xxxxxxxxxx${stock_name}xxxxx'

    for key,value in a.items():
        b=b.replace('${' + key + '}',repr(value))
    print(b)
