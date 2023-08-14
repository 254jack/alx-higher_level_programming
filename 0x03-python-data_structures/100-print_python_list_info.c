#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - a fucntion that prints basic
 * info about a Python list
 * @p: PyObject pointer to the Python list
 */
void print_python_list_info(PyObject *p);

int main(void)
{
    Py_Initialize();

    PyObject *list = PyList_New(0);
    PyList_Append(list, PyLong_FromLong(42));
    PyList_Append(list, PyUnicode_DecodeUTF8("Hello", 5, NULL));

    print_python_list_info(list);

    Py_DECREF(list);
    Py_Finalize();

    return 0;
}

/**
 * print_python_list_info - a function that prints basic
 * info about a Python list
 * @p: PyObject pointer to the Python list
 */
void print_python_list_info(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    int size = PyList_Size(p);
    int allocated = list->allocated;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", allocated);

    for (int i = 0; i < size; i++)
    {
        PyObject *element = PyList_GetItem(p, i);
        const char *typeName = Py_TYPE(element)->tp_name;
        printf("Element %d: %s\n", i, typeName);
    }
}
