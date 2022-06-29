import csv
import random
import datetime
import exrex
import time


def generate_company_name(companies):
    category = random.choice([company for company in companies.keys()])
    company = random.choice(companies[category])
    return {'company': company.upper(), 'category': category}


def generate_date():
    start = datetime.date(2017, 2, 15)
    end = datetime.date(2023, 11, 11)
    day_diff = (end - start).days
    random_diff = random.randrange(day_diff)
    random_date = (start +
                   datetime.timedelta(days=random_diff)).strftime('%-d/%-m/%y')
    return random_date


def generate_time():
    hh = '{}'.format(random.randrange(1, 12))
    mm = '{}'.format(random.randrange(0, 59)).rjust(2, '0')
    time = hh + ':' + mm
    time += " {}".format(random.choice(['AM', 'PM']))
    return time


def generate_amount():
    amount = "%.2f" % random.randrange(10, 70000)
    return amount


def generate_recipient_name():
    fname = exrex.getone('([A-Z]{1})(a|e|i|o|u){1,2}[a-z]{1,2}')
    lname = exrex.getone('([A-Z]{1})(a|e|i|o|u){1,2}[a-z]{1,2}')
    name = fname + ' ' + lname
    return name.upper()


def generate_phone_no():
    phone = exrex.getone('07\d{8}')
    return phone


def generate_mpesa_code():
    code = exrex.getone('([A-Z]|\d){10}')
    return code


def sent_to_company():
    companies = {
        'airtime': ['Safaricom Offers', 'Safaricom Limited'],
        'parking': ['PAYTECH LIMITED'],
    }
    selected_company = generate_company_name(companies)
    account = ' Tunukiwa' if selected_company[
        'company'] == 'Safaricom Offers'.upper() else ''
    message = 'Ksh{} sent to {} for account{} on {} at {}'.format(
        generate_amount(), selected_company['company'], account,
        generate_date(), generate_time())

    return {'sms': message, 'category': selected_company['category']}


def paid_to_company():
    companies = {
        'shopping': [
            'naivas supermarket', 'carrefour', 'quick mart', 'tuskys',
            'kamindi', 'Speedaf Logistics kenya ltd'
        ],
        'fuel': ['Total', 'Shell', 'Rubis', 'Astrol', 'Simco'],
    }
    selected_company = generate_company_name(companies)
    message = 'Ksh{} paid to {} on {} at {}'.format(
        generate_amount(), selected_company['company'], generate_date(),
        generate_time())

    return {'sms': message, 'category': selected_company['category']}


def sent_to_person():
    message = 'Ksh{} sent to {} {} on {} at {}'.format(
        generate_amount(), generate_recipient_name(), generate_phone_no(),
        generate_date(), generate_time())
    return {'sms': message, 'category': 'mobile money'}


def received_from_person():
    message = 'You have received Ksh{} from {} {} on {} at {}'.format(
        generate_amount(), generate_recipient_name(), generate_phone_no(),
        generate_date(), generate_time())
    return {'sms': message, 'category': 'mobile money'}


def mshwari_received():
    message = 'Your M-Shwari loan has been approved on {} {} and Ksh{} has been deposited to your M-PESA account'.format(
        generate_date(), generate_time(), generate_amount())
    return {'sms': message, 'category': 'loan'}


def generate_banks():
    banks = ['IM Bank', 'NCBA Loop', 'Equity']
    return banks


def received_from_bank():
    pass


def sent_to_bank():
    pass


def sent_to_money_market():
    pass


def sent_to_sacco():
    pass


def sent_to_bank_paybill():
    pass


def electricity_payment():
    pass


def write_csv():
    start_time = time.time()
    functions = [
        sent_to_company, paid_to_company, sent_to_person, received_from_person,
        mshwari_received
    ]

    with open(
            '/home/dev-pc-3/Documents/jipange/backend/Machine Learning/info.csv',
            'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"')

        for i in range(40000):
            payload = random.choice(functions)()
            category = payload['category']
            message = payload['sms']
            balance = generate_amount()
            code = generate_mpesa_code()
            message = "{} confirmed. {}. New M-PESA balance is Ksh{}.".format(
                code, message, balance)
            writer.writerow([message, category])

    print("--- %.2f seconds ---" % (time.time() - start_time))


write_csv()
