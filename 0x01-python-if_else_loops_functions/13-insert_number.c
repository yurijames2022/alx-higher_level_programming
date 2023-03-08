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
	listint_t *current, *prev, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}

	new->n = number;
	new->next = NULL;

	current = *head;
	while (current && current->n < new->n)
	{
		prev = current;
		current = current->next;

	}

	if (prev == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		prev->next = new;
		new->next = current;
	}
	return (new);
}
