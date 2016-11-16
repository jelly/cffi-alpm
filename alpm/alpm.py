from alpm.list import AlpmList
from alpm._alpm import ffi, lib

root = ffi.new('char[]', b'/')
dbpath = ffi.new('char[]', b'/var/lib/pacman/')
errno = ffi.new('alpm_errno_t *')
handle = lib.alpm_initialize(root, dbpath, errno)

db = lib.alpm_get_localdb(handle)

targets = AlpmList()
targets.add(b'pacman')

def db_search(db, targets):
    results = AlpmList(lib.alpm_db_search(db, targets.list))
    packages = []

    for result in results:
        pkg = ffi.cast('alpm_pkg_t *', result)
        pkgname = ffi.cast('char *', lib.alpm_pkg_get_name(pkg))
        if pkgname:
            pkgname = ffi.string(pkgname)
            print(pkgname.decode())

db_search(db, targets)
