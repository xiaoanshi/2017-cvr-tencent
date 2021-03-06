# _*_ coding: utf-8 _*_
from csv import DictReader
import sys
from datetime import datetime

data_path = '../../data/'
save_path = '../../output/vw/'


def vw_train():
    with open(save_path + 'train.vw', 'w') as outfile:

        for t, row in enumerate(DictReader(open(data_path + 'train-ctr.csv', 'r'))):

            categorical_features = []
            for k, v in row.items():
                if k not in ['label']:
                    if len(str(v)) > 0:
                        categorical_features.append('{0}:{1}'.format(k, v))

            if row['label'] == '1':
                label = 1
            else:
                label = -1

            outfile.write('{0} \' |categorical {1}\n'.format(label, ' '.join(['{0}'.format(val) for val
                                                                              in categorical_features])))
            if t % 100000 == 0:
                print(datetime.now(), 'Line processed: {0}'.format(t))


def vw_test():
    with open(save_path + 'test.vw', 'w') as outfile, open(data_path + 'validation.csv', 'w') as f_va:
        f_va.write('id,label\n')
        for t, row in enumerate(DictReader(open(data_path + 'test-ctr.csv', 'r'))):
            f_va.write(str(t) + ',' + row['label'] + '\n')
            categorical_features = []
            for k, v in row.items():
                if k not in ['label']:
                    if len(str(v)) > 0:
                        categorical_features.append('{0}:{1}'.format(k, v))

            if row['label'] == '1':
                label = 1
            else:
                label = -1

            outfile.write('{0} \' |categorical {1}\n'.format(label, ' '.join(['{0}'.format(val) for val
                                                                              in categorical_features])))
            if t % 100000 == 0:
                print(datetime.now(), 'Line processed: {0}'.format(t))
    f_va.close()


if __name__ == '__main__':
    vw_train()
    vw_test()
