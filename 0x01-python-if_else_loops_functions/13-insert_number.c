#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of the first node of listint_t list
 * @number: integer to be included in the new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *n_node, *crrnt;

    n_node = malloc(sizeof(listint_t));
    if (n_node == NULL)
        return (NULL);

    n_node->n = number;
    n_node->next = NULL;

    if (*head == NULL || number < (*head)->n)
    {
        n_node->next = *head;
        *head = n_node;
        return (n_node);
    }

    crrnt = *head;
    while (crrnt->next != NULL && crrnt->next->n < number)
        crrnt = crrnt->next;

    n_node->next = crrnt->next;
    crrnt->next = n_node;

    return (n_node);
}
