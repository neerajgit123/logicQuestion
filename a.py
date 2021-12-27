d={'is_running': False, 'pending_approval': False, 'comment': None, 'approver_comment': 'dfxfgfdxgfd', 'data': [{'name': 'sddsf', 'category': 'Divesture', 'effective_date': '2021-12-09', 'status': 'Pending Approval', 'fincial_informations': '/media/fincial/file_example_XLS_50 (1).xls', 'loss_estimations': '/media/loseestimation/shakshya_ABC_imeNH9r.xls'}, {'name': 'hello', 'category': 'M&A', 'effective_date': '2021-12-05', 'status': 'Pending Approval', 'fincial_informations': '/media/fincial/shakshya_ABC.xls', 'loss_estimations': '/media/loseestimation/shakshya_XYZ.xls'}, {'name': 'DSFDSF', 'category': 'M&A', 'effective_date': '2021-12-11', 'status': 'SDFA', 'fincial_informations': '/media/fincial/shakshya_ABC_ObMKK6t.xls', 'loss_estimations': '/media/loseestimation/shakshya_XYZ_qwlZonj.xls'}, {'name': 'sasdwd', 'category': 'Divesture', 'effective_date': '2021-12-25', 'status': 'Pending Approval', 'fincial_informations': '/media/fincial/shakshya_XYZ%20(1)_TVdbiFU.xls', 'loss_estimations': None}, {'name': 'qsadqwdwqe', 'category': 'M&A', 'effective_date': '2021-12-23', 'status': 'Pending Approval', 'fincial_informations': '/media/fincial/shakshya_XYZ_jo1d27e.xls', 'loss_estimations': '/media/loseestimation/shakshya_XYZ%20(1)_VLb3hUF.xls'}]}


if d['data'][0]['status']=='Pending Approval':
    d['data'][0]['status']='Approved'
print(d)
    
