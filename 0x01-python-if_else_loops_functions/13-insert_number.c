#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - A function that inserts a number into a sorted singly list
 * @head: The head of the list
 * @number: The number to be added
 * Return: The address of the new node or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *new, *current, *nxt;

	current = *head;
	nxt = current->next;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}

	new->n = number;

	while (nxt->n < new->n)
	{
		prev = nxt;
		nxt = nxt->next;

	}
	new->next = nxt;
	prev->next = new;

	return (new);
}
