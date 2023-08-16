#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - a function that rints information 
 * about Python bytes objects
 * @p: Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);

	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first %d bytes:", (int)(size > 10 ? 10 : size));
	for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); ++i)
	{
		printf(" %02x", PyBytes_AsString(p)[i] & 0xff);
	}
	printf("\n");
}

/**
 * print_python_list - a function that prints information 
 * about Python lists
 * @p: Python list object
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[.] Python list info\n");
		printf("  [ERROR] Invalid Python List\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %ld: ", i);
		if (PyBytes_Check(item))
		{
			print_python_bytes(item);
		}
		else if (PyLong_Check(item))
		{
			printf("int\n");
		}
		else if (PyFloat_Check(item))
		{
			printf("float\n");
		}
		else if (PyTuple_Check(item))
		{
			printf("tuple\n");
		}
		else if (PyList_Check(item))
		{
			printf("list\n");
		}
		else if (PyUnicode_Check(item))
		{
			printf("str\n");
		}
		else
		{
			printf("unknown\n");
		}
	}
}

PyMODINIT_FUNC PyInit_libPython(void)
{
	return NULL;
}
