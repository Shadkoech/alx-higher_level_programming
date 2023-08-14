#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 *print_python_list_info - Gives basics on python lists(under the hood)
 *@p: pointer to Python Object
 *
 *Return: Nothing(void)
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t x = 0;
	const char *type_name;
	Py_ssize_t list_len;
	PyObject *item;

	list_len = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", list_len);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (x = 0; x < list_len; x++)
	{
		item = PyList_GetItem(p, x);
		type_name = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", x, type_name);
	}
}
