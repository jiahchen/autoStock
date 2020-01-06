import twstock
import time
import requests
import json

def get_all_company():
    origin_code_list = list(twstock.codes.keys())
    result_list = []
    for code in origin_code_list:
        code_info = twstock.codes.get(code)
        if code_info.CFI == 'ESVUFR' and code_info.market == '\u4e0a\u5e02':
            result_list.append(code)
    return result_list

def get_EOD_info(code, day):
    url = 'https://fund.bot.com.tw/Z/ZC/ZCW/CZKC1.djbcd?a={code}&b=D&c={day}'.format(code=code, day=day)
    try:
        res = requests.get(url, headers=None, timeout=8)
    except requests.exceptions.RequestException:
        res = "error"
    res = res.text if res.status_code < 210 else "error_code"
    return info_parser(res)

def info_parser(info):
    info_dict = {
        'date': [],
        'start': [],
        'high': [],
        'low': [],
        'over': [],
        'volume': [],
        'mt': [],
        'ss': [],
        'foreign_amount': [],
        'trust_amount': [],
        'self_amount': [],
        'pass_info1': [],
        'pass_info2': [],
        'pass_info3': [],
        'jp_total_amount': [],
        'pass_info4': [],
        'mt_ss_sum': [],
        'mt_usage': [],
        'ss_usage': [],
        'foreign_buy': [],
        'trust_buy': [],
        'self_buy': [],
        'jp_total_buy': []
    }
    for (data, key) in zip(info.split(), list(info_dict.keys())):
        info_dict[key] = data
    return info_dict

def main():
    company_list = get_all_company()

    for code in company_list:
        print(code + ': [' + get_EOD_info(code, 2)['over'] + ']')

    for i in range(len(company_list)):
        result = json.dumps(twstock.realtime.get(company_list[:i]))
        print(result['success'])
        print('==> ' + str(i))
        time.sleep(2)


if __name__ == '__main__':
    main()