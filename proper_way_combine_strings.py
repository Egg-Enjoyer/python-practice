def fake_bin(x):
    result_list = []
    for i in x:
        if int(i) < 5:
            result_list.append("0")
        else:
            result_list.append("1")
    return "".join(result_list)
