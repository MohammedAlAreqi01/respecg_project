import wfdb
import numpy as np

def load_record(record_name, data_dir='data/'):
    path = f'{data_dir}{record_name}'
    record = wfdb.rdrecord(path)
    signal = record.p_signal[:, 0]
    fs = record.fs

    try:
        apnea_ann = wfdb.rdann(path, 'apn')
    except FileNotFoundError:
        apnea_ann = None

    return signal, fs, apnea_ann
