import time
import loader
from tester import MongoTester

if __name__ == '__main__':
    environment = 'Staging'

    # Load environment information
    env_info = loader.load_csv_file('data/globaldata.csv')
    for env in env_info:
        if env['environment'] == environment:
            env_info = env
            break
    print(repr(env_info))
    mdydatastore_tester = MongoTester(env_info['mdydatastore_host'], env_info['mdydatastore_port'], 'mdydatastore',
                                      env_info['mdydatastore_username'], env_info['mdydatastore_password'])
    ods_tester = MongoTester(env_info['ods_host'], env_info['ods_port'], 'ODS',
                             env_info['ods_username'], env_info['ods_password'])

    # Load test cases
    test_info = loader.load_xlsx_file('data/testdata.xlsx')

    # Run test cases
    for test in test_info:
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), test['Feature'])
        if test['Query'] is None:
            break
        if str(test['Database']).strip().lower() == 'mdydatastore':
            mdydatastore_tester.run(test['Query'], test['ExpectedResults'])
        elif str(test['Database']).strip().lower() == 'ods':
            ods_tester.run(test['Query'], test['ExpectedResults'])
        else:
            print('ERROR: Can not find db info: ' + str(test))
