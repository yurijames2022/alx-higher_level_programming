#include "lists.h"
/**
 * check_cycle - A function that checks for cycle in list
 * @list: The list to be checked
 * Return: 0 if no cycle, 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);

	}
	return (0);

}
