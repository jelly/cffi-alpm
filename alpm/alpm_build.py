from cffi import FFI

ffibuilder = FFI()
ffibuilder.set_source("alpm._alpm",
    r"""
    #include <alpm.h>
    #include <alpm_list.h>
    """,
    libraries=['alpm'])
ffibuilder.cdef("""
    /* alpm_list */
    typedef struct __alpm_list_t {
        /** data held by the list node */
        void *data;
        /** pointer to the previous node */
        struct __alpm_list_t *prev;
        /** pointer to the next node */
        struct __alpm_list_t *next;
    } alpm_list_t;
    alpm_list_t *alpm_list_add(alpm_list_t *list, void *data);
    alpm_list_t *alpm_list_next(const alpm_list_t *list);


    /* alpm */

    typedef struct __alpm_handle_t alpm_handle_t;
    typedef struct __alpm_db_t alpm_db_t;
    typedef struct __alpm_pkg_t alpm_pkg_t;
    typedef enum _alpm_errno_t alpm_errno_t;

    alpm_handle_t *alpm_initialize(const char *root, const char *dbpath, alpm_errno_t *err);
    int alpm_release(alpm_handle_t *handle);

    // database
    alpm_db_t *alpm_get_localdb(alpm_handle_t *handle);
    alpm_list_t *alpm_db_search(alpm_db_t *db, const alpm_list_t *needles);
    alpm_pkg_t *alpm_db_get_pkg(alpm_db_t *db, const char *name);

    // package
    alpm_pkg_t *alpm_find_satisfier(alpm_list_t *pkgs, const char *depstring);
    const char *alpm_pkg_get_name(alpm_pkg_t *pkg);
""")

if __name__ == '__main__':
    ffibuilder.compile(verbose=True)
