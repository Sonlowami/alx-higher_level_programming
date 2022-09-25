#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - print python list info
 * @p: An object of type Pyobject representing list
 */
void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject *px = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", px->allocated);
	for (i = 0; i < PyList_Size(p); i++)
		printf("Element %d: %s\n", i, Py_TYPE(px->ob_item[i])->tp_name);
}
