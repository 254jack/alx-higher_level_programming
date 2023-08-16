#include <Python.h>
#include <stdio.h>
#include <wchar.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - a function that prints basic information
 * about Python lists
 * @p: PyObject pointer to a Python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *item;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - a function that prints basic information 
 * about Python bytes objects
 * @p: PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	wchar_t *data;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_GET_SIZE(p);
	data = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %ls\n", data);

	printf("  first %ld bytes:", size > 10 ? 10 : size);
	for (i = 0; i < size && i < 10; i++)
		printf(" %02x", data[i] & 0xff);
	printf("\n");
}

PyMODINIT_FUNC PyInit_libPython(void)
{
	return NULL;
}
