import sys as __sys
if not __sys.warnoptions:
    import os as __os
    import warnings as __warnings
    __warnings.filterwarnings("default",category=DeprecationWarning,module='icarus-bt') # Change the filter in this process
    __os.environ["PYTHONWARNINGS"] = "default::DeprecationWarning:icarus-bt"            # Also affect subprocesses

if __sys.version_info <= (3, 10):
    __warnings.filterwarnings("default",category=ImportWarning,module='icarus-bt')   # Change the filter in this process
    __os.environ["PYTHONWARNINGS"] = "default::ImportWarning:icarus-bt"              # Also affect subprocesses
    __warnings.warn('\n\n ================================================================= '+
                    '\n\n    WARNING: `icarus-bt` is NOT supported for Python versions '+
                    '\n               less than 3.10'
                    '\n\n ================================================================= ',
                    category=ImportWarning)
