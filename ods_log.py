from glob import glob
from odswriter import writer, Formula
from time import time, ctime, sleep

sec_sleep = 60
t = time()
while True:
    ls_dl = glob('N:/nchc/log_dl/users\\dl_*.csv')
    ls_vdi = glob('N:/nchc/log_vdi/users\\vdi_*.csv')
    accounts = {
        name_dl.replace('N:/nchc/log_dl/users\\dl_', '').replace('.csv', '')
        for name_dl in ls_dl
    } | {
        name_vdi.replace('N:/nchc/log_vdi/users\\vdi_', '').replace('.csv', '')
        for name_vdi in ls_vdi
    }

    for name in accounts:
        try:
            with writer(open(
                'N:/nchc/log/{}.ods'.format(name), 'wb'
            )) as out_ods:
                out_total = out_ods.new_sheet('total')
                
                out_dl = out_ods.new_sheet('Deadline')
                data_dl = ('SU_total', 0.)
                name_dl = 'N:/nchc/log_dl/users\\dl_{}.csv'.format(name)
                if name_dl in ls_dl:
                    with open(name_dl, encoding='utf-8') as in_dl:
                        out_dl.writerow(next(in_dl).strip().split('\t'))
                        for data_dl in in_dl:
                            data_dl = data_dl.strip().split('\t')
                            if data_dl:
                                if 'SU_total' == data_dl[0]:
                                    data_dl[1] = float(data_dl[1])
                                else:
                                    data_dl[3] = int(data_dl[3])
                                    data_dl[5] = float(data_dl[5])
                                    data_dl[6] = float(data_dl[6])
                            out_dl.writerow(data_dl)
                
                out_vdi = out_ods.new_sheet('VDI')
                data_vdi = ('SU_total', 0.)
                name_vdi = 'N:/nchc/log_vdi/users\\vdi_{}.csv'.format(name)
                if name_vdi in ls_vdi:
                    with open(name_vdi, encoding='utf-8') as in_vdi:
                        out_vdi.writerow(next(in_vdi).strip().split('\t'))
                        for data_vdi in in_vdi:
                            data_vdi = data_vdi.strip().split('\t')
                            if data_vdi:
                                if 'SU_total' == data_vdi[0]:
                                    data_vdi[1] = float(data_vdi[1])
                                else:
                                    data_vdi[2] = float(data_vdi[2])
                                    data_vdi[4] = float(data_vdi[4])
                                    data_vdi[5] = float(data_vdi[5])
                            out_vdi.writerow(data_vdi)
                
                out_total.writerow(('Deadline', data_dl[1]))
                out_total.writerow(('VDI', data_vdi[1]))
                out_total.writerow(('total', Formula('B1+B2')))
            
        except OSError:
            pass
    
    print('\r\t\t\t', round(time() - t, 3), ctime(), end='     ')
    sleep(sec_sleep)
