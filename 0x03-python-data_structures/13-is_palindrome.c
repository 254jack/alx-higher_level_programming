#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    int values[10000];  // Assuming a maximum of 10000 elements (you can adjust this)

    int i = 0;
    while (current != NULL)
    {
        values[i] = current->n;
        current = current->next;
        i++;
    }

    int left = 0;
    int right = i - 1;

    while (left < right)
    {
        if (values[left] != values[right])
            return 0;
        left++;
        right--;
    }
    return 1;
}
