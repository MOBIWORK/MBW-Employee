import mbw_employee
import i18n
import os

base_file_path = os.path.dirname(mbw_employee.__file__)
i18n.load_path.append(base_file_path + '/translations')
