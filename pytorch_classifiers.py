from model_wraper import MLP_Wrapper_A, MLP_Wrapper_B, MLP_Wrapper_C, MLP_Wrapper_D, MLP_Wrapper_E, MLP_Wrapper_F
from utils import read_json
import numpy as np


def mlp_A_train(exp_idx, repe_time, accu, config):
    mlp_setting = config
    for i in range(repe_time):
        mlp = MLP_Wrapper_A(imbalan_ratio=mlp_setting['imbalan_ratio'],
                            fil_num=mlp_setting['fil_num'],
                            drop_rate=mlp_setting['drop_rate'],
                            batch_size=mlp_setting['batch_size'],
                            balanced=mlp_setting['balanced'],
                            roi_threshold=mlp_setting['roi_threshold'],
                            roi_count=mlp_setting['roi_count'],
                            choice=mlp_setting['choice'],
                            exp_idx=exp_idx,
                            seed=seed+i,
                            model_name='mlp_A',
                            metric='accuracy')
        mlp.train(lr=mlp_setting['learning_rate'],
                  epochs=mlp_setting['train_epochs'])
        accu_test, accu_AIBL, accu_NACC, accu_FHS = mlp.test(i)[2:]
        accu['A']['test'].append(accu_test)
        accu['A']['NACC'].append(accu_NACC)
        accu['A']['AIBL'].append(accu_AIBL)
        accu['A']['FHS'].append(accu_FHS)


def mlp_B_train(exp_idx, repe_time, accu, config):
    mlp_setting = config
    for i in range(repe_time):
        mlp = MLP_Wrapper_B(imbalan_ratio=mlp_setting['imbalan_ratio'],
                            fil_num=mlp_setting['fil_num'],
                            drop_rate=mlp_setting['drop_rate'],
                            batch_size=mlp_setting['batch_size'],
                            balanced=mlp_setting['balanced'],
                            roi_threshold=mlp_setting['roi_threshold'],
                            roi_count=mlp_setting['roi_count'],
                            choice=mlp_setting['choice'],
                            exp_idx=exp_idx,
                            seed=seed+i,
                            model_name='mlp_B_BN',
                            metric='accuracy')
        mlp.train(lr=mlp_setting['learning_rate'],
                  epochs=mlp_setting['train_epochs'])
        accu_test, accu_AIBL, accu_NACC, accu_FHS = mlp.test(i)[2:]
        accu['B']['test'].append(accu_test)
        accu['B']['NACC'].append(accu_NACC)
        accu['B']['AIBL'].append(accu_AIBL)
        accu['B']['FHS'].append(accu_FHS)


def mlp_C_train(exp_idx, repe_time, accu, config):
    mlp_setting = config
    for i in range(repe_time):
        mlp = MLP_Wrapper_C(imbalan_ratio=mlp_setting['imbalan_ratio'],
                            fil_num=mlp_setting['fil_num'],
                            drop_rate=mlp_setting['drop_rate'],
                            batch_size=mlp_setting['batch_size'],
                            balanced=mlp_setting['balanced'],
                            roi_threshold=mlp_setting['roi_threshold'],
                            roi_count=mlp_setting['roi_count'],
                            choice=mlp_setting['choice'],
                            exp_idx=exp_idx,
                            seed=seed+i,
                            model_name='mlp_C_BN',
                            metric='accuracy')
        mlp.train(lr=mlp_setting['learning_rate'],
                  epochs=mlp_setting['train_epochs'])
        accu_test, accu_AIBL, accu_NACC, accu_FHS = mlp.test(i)[2:]
        accu['C']['test'].append(accu_test)
        accu['C']['NACC'].append(accu_NACC)
        accu['C']['AIBL'].append(accu_AIBL)
        accu['C']['FHS'].append(accu_FHS)


def mlp_E_train(exp_idx, repe_time, accu, config):
    mlp_setting = config
    for i in range(repe_time):
        mlp = MLP_Wrapper_E(imbalan_ratio=mlp_setting['imbalan_ratio'],
                            fil_num=mlp_setting['fil_num'],
                            drop_rate=mlp_setting['drop_rate'],
                            batch_size=mlp_setting['batch_size'],
                            balanced=mlp_setting['balanced'],
                            roi_threshold=mlp_setting['roi_threshold'],
                            roi_count=mlp_setting['roi_count'],
                            choice=mlp_setting['choice'],
                            exp_idx=exp_idx,
                            seed=seed+i,
                            model_name='mlp_E',
                            metric='accuracy')
        mlp.train(lr=mlp_setting['learning_rate'],
                  epochs=mlp_setting['train_epochs'])
        accu_test, accu_AIBL, accu_NACC, accu_FHS = mlp.test(i)[2:]
        accu['E']['test'].append(accu_test)
        accu['E']['NACC'].append(accu_NACC)
        accu['E']['AIBL'].append(accu_AIBL)
        accu['E']['FHS'].append(accu_FHS)


def mlp_F_train(exp_idx, repe_time, accu, config):
    mlp_setting = config
    for i in range(repe_time):
        mlp = MLP_Wrapper_F(imbalan_ratio=mlp_setting['imbalan_ratio'],
                            fil_num=mlp_setting['fil_num'],
                            drop_rate=mlp_setting['drop_rate'],
                            batch_size=mlp_setting['batch_size'],
                            balanced=mlp_setting['balanced'],
                            roi_threshold=mlp_setting['roi_threshold'],
                            roi_count=mlp_setting['roi_count'],
                            choice=mlp_setting['choice'],
                            exp_idx=exp_idx,
                            seed=seed+i,
                            model_name='mlp_F',
                            metric='accuracy')
        mlp.train(lr=mlp_setting['learning_rate'],
                  epochs=mlp_setting['train_epochs'])
        accu_test, accu_AIBL, accu_NACC, accu_FHS = mlp.test(i)[2:]
        accu['F']['test'].append(accu_test)
        accu['F']['NACC'].append(accu_NACC)
        accu['F']['AIBL'].append(accu_AIBL)
        accu['F']['FHS'].append(accu_FHS)


def mlp_D_train(exp_idx, repe_time, accu, config):
    mlp_setting = config
    for i in range(repe_time):
        mlp = MLP_Wrapper_D(imbalan_ratio=mlp_setting['imbalan_ratio'],
                            fil_num=mlp_setting['fil_num'],
                            drop_rate=mlp_setting['drop_rate'],
                            batch_size=mlp_setting['batch_size'],
                            balanced=mlp_setting['balanced'],
                            exp_idx=exp_idx,
                            seed=seed + i,
                            model_name='mlp_D',
                            metric='accuracy')
        mlp.train(lr=mlp_setting['learning_rate'],
                  epochs=mlp_setting['train_epochs'])
        accu_test, accu_AIBL, accu_NACC, accu_FHS = mlp.test(i)[2:]
        accu['D']['test'].append(accu_test)
        accu['D']['NACC'].append(accu_NACC)
        accu['D']['AIBL'].append(accu_AIBL)
        accu['D']['FHS'].append(accu_FHS)


def mlp():
    accu = {'A':{'test':[], 'NACC':[], 'AIBL':[], 'FHS':[]}, \
            'B':{'test':[], 'NACC':[], 'AIBL':[], 'FHS':[]}, \
            'C':{'test':[], 'NACC':[], 'AIBL':[], 'FHS':[]}}

    for exp_idx in range(5):
        print('B')
        mlp_B_train(exp_idx, 3, accu)
        print('C')
        mlp_C_train(exp_idx, 3, accu)
        print('A')
        mlp_A_train(exp_idx, 3, accu)

    print('ADNI test accuracy ',
          'A {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['A']['test'])), float(np.std(accu['A']['test']))), \
          'B {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['B']['test'])), float(np.std(accu['B']['test']))), \
          'C {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['C']['test'])), float(np.std(accu['C']['test']))))
    print('NACC test accuracy ',
          'A {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['A']['NACC'])), float(np.std(accu['A']['NACC']))), \
          'B {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['B']['NACC'])), float(np.std(accu['B']['NACC']))), \
          'C {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['C']['NACC'])), float(np.std(accu['C']['NACC']))))
    print('AIBL test accuracy ',
          'A {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['A']['AIBL'])), float(np.std(accu['A']['AIBL']))), \
          'B {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['B']['AIBL'])), float(np.std(accu['B']['AIBL']))), \
          'C {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['C']['AIBL'])), float(np.std(accu['C']['AIBL']))))
    print('FHS test accuracy  ',
          'A {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['A']['FHS'])), float(np.std(accu['A']['FHS']))), \
          'B {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['B']['FHS'])), float(np.std(accu['B']['FHS']))), \
          'C {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['C']['FHS'])), float(np.std(accu['C']['FHS']))))

##############################################################################################
# roi count meshgrid
def mlp_A_valid(exp_idx, repe_time, accu, config):
    mlp_setting = config
    for i in range(repe_time):
        mlp = MLP_Wrapper_A(imbalan_ratio=mlp_setting['imbalan_ratio'],
                            fil_num=mlp_setting['fil_num'],
                            drop_rate=mlp_setting['drop_rate'],
                            batch_size=mlp_setting['batch_size'],
                            balanced=mlp_setting['balanced'],
                            roi_threshold=mlp_setting['roi_threshold'],
                            roi_count=mlp_setting['roi_count'],
                            choice=mlp_setting['choice'],
                            exp_idx=exp_idx,
                            seed=seed+i,
                            model_name='mlp_A_non_filter',
                            metric='accuracy')
        mlp.train(lr=mlp_setting['learning_rate'],
                  epochs=mlp_setting['train_epochs'])
        accu_valid = mlp.test(i)[1]
        accu['A']['valid'].append(accu_valid)


def mlp_A_count(config):
    print('##################################################')
    print(config)
    accu = {'A':{'valid':[]}}
    for exp_idx in range(5):
        mlp_A_valid(exp_idx, 1, accu, config)
    print('ADNI valid accuracy ',
          'A {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['A']['valid'])), float(np.std(accu['A']['valid']))))
# roi count meshgrid
###################################################################################################


def mlp_A(config):
    print('##################################################')
    print(config)
    accu = {'A':{'test':[], 'NACC':[], 'AIBL':[], 'FHS':[]}}
    for exp_idx in range(5):
        # print(exp_idx)
        mlp_A_train(exp_idx, 3, accu, config)
    print('ADNI test accuracy ',
          'A {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['A']['test'])), float(np.std(accu['A']['test']))))
    print('NACC test accuracy ',
          'A {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['A']['NACC'])), float(np.std(accu['A']['NACC']))))
    print('AIBL test accuracy ',
          'A {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['A']['AIBL'])), float(np.std(accu['A']['AIBL']))))
    print('FHS test accuracy  ',
          'A {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['A']['FHS'])), float(np.std(accu['A']['FHS']))))


def mlp_B(config):
    print('##################################################')
    print(config)
    accu = {'B':{'test':[], 'NACC':[], 'AIBL':[], 'FHS':[]}}
    for exp_idx in range(5):
        mlp_B_train(exp_idx, 3, accu, config)
    print('ADNI test accuracy ',
          'B {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['B']['test'])), float(np.std(accu['B']['test']))))
    print('NACC test accuracy ',
          'B {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['B']['NACC'])), float(np.std(accu['B']['NACC']))))
    print('AIBL test accuracy ',
          'B {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['B']['AIBL'])), float(np.std(accu['B']['AIBL']))))
    print('FHS test accuracy  ',
          'B {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['B']['FHS'])), float(np.std(accu['B']['FHS']))))


def mlp_C(config):
    print('##################################################')
    print(config)
    accu = {'C':{'test':[], 'NACC':[], 'AIBL':[], 'FHS':[]}}
    for exp_idx in range(5):
        mlp_C_train(exp_idx, 3, accu, config)
    print('ADNI test accuracy ',
          'C {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['C']['test'])), float(np.std(accu['C']['test']))))
    print('NACC test accuracy ',
          'C {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['C']['NACC'])), float(np.std(accu['C']['NACC']))))
    print('AIBL test accuracy ',
          'C {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['C']['AIBL'])), float(np.std(accu['C']['AIBL']))))
    print('FHS test accuracy  ',
          'C {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['C']['FHS'])), float(np.std(accu['C']['FHS']))))


def mlp_D(config):
    print('##################################################')
    print(config)
    accu = {'D':{'test':[], 'NACC':[], 'AIBL':[], 'FHS':[]}}
    for exp_idx in range(5):
        mlp_D_train(exp_idx, 3, accu, config)
    print('ADNI test accuracy ',
          'D {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['D']['test'])), float(np.std(accu['D']['test']))))
    print('NACC test accuracy ',
          'D {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['D']['NACC'])), float(np.std(accu['D']['NACC']))))
    print('AIBL test accuracy ',
          'D {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['D']['AIBL'])), float(np.std(accu['D']['AIBL']))))
    print('FHS test accuracy  ',
          'D {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['D']['FHS'])), float(np.std(accu['D']['FHS']))))


def mlp_E(config):
    print('##################################################')
    print(config)
    accu = {'E':{'test':[], 'NACC':[], 'AIBL':[], 'FHS':[]}}
    for exp_idx in range(5):
        mlp_E_train(exp_idx, 3, accu, config)
    print('ADNI test accuracy ',
          'E {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['E']['test'])), float(np.std(accu['E']['test']))))
    print('NACC test accuracy ',
          'E {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['E']['NACC'])), float(np.std(accu['E']['NACC']))))
    print('AIBL test accuracy ',
          'E {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['E']['AIBL'])), float(np.std(accu['E']['AIBL']))))
    print('FHS test accuracy  ',
          'E {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['E']['FHS'])), float(np.std(accu['E']['FHS']))))


def mlp_F(config):
    print('##################################################')
    print(config)
    accu = {'F':{'test':[], 'NACC':[], 'AIBL':[], 'FHS':[]}}
    for exp_idx in range(5):
        mlp_F_train(exp_idx, 3, accu, config)
    print('ADNI test accuracy ',
          'F {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['F']['test'])), float(np.std(accu['F']['test']))))
    print('NACC test accuracy ',
          'F {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['F']['NACC'])), float(np.std(accu['F']['NACC']))))
    print('AIBL test accuracy ',
          'F {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['F']['AIBL'])), float(np.std(accu['F']['AIBL']))))
    print('FHS test accuracy  ',
          'F {0:.4f}+/-{1:.4f}'.format(float(np.mean(accu['F']['FHS'])), float(np.std(accu['F']['FHS']))))


if __name__ == "__main__":
    config = read_json('./config.json')
    seed = 1000

    # config['mlp_A']['choice'] = 'thres'
    # config['mlp_A']['roi_threshold'] = -2
    # mlp_A_count(config['mlp_A'])

    # for count in [20, 50, 100, 200, 400, 800, 1600]:
    #     config['mlp_A']["roi_count"] = count
    #     mlp_A_count(config['mlp_A'])

    # mlp_A(config["mlp_A"])
    # mlp_B(config["mlp_B"])
    mlp_C(config["mlp_C"])
    # mlp_D(config["mlp_D"])
    # mlp_E(config["mlp_E"])
    # mlp_F(config['mlp_F'])

    