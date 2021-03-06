from parse_utils import parse_date

# files
fname_personal = 'data/personal_info.csv'
fname_employment = 'data/employment.csv'
fname_vehicles = 'data/vehicles.csv'
fname_update_status = 'data/update_status.csv'
fnames = fname_personal, \
         fname_employment, \
         fname_vehicles, \
         fname_update_status

# Parsers
personal_parser = (str, str, str, str, str)
employment_parser = (str, str, str, str)
vehicles_parser = (str, str, str, int)
pdate_status_parser = (str, parse_date, parse_date)
parsers = personal_parser, \
          employment_parser, \
          vehicles_parser, \
          pdate_status_parser

# Named Tuple Names
personal_class_name = 'Personal'
employment_class_name = 'Employment'
vehicles_class_name = 'Vehicles'
update_status_class_name = 'UpdateStatus'
class_names = personal_class_name, \
              employment_class_name, \
              vehicles_class_name, \
              update_status_class_name

# Field Inclusion/Exclusion
personal_fields_compress = [True, True, True, True, True]
employment_fields_compress = [True, True, True, False]
vehicles_fields_compress = [False, True, True, True]
update_status_fields_compress = [False, True, True]
compress_fields = personal_fields_compress, \
                  employment_fields_compress, \
                  vehicles_fields_compress, \
                  update_status_fields_compress
