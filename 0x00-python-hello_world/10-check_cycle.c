#include "lists.h"
/**
 * check_cycle - check if a linkedlist loops
 * @list: pointer to the head of the list
 *
 * Return: 1 if found, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *node_a, *node_b;

	node_a = list, node_b = list->next;
	while (node_a && node_b)
	{
		if (node_a == node_b)
			return (1);
		/*if node_b is twice faster, it will catch node_a in the cycle*/
		node_a = node_a->next;
		if (!node_b->next)
			break;
		node_b = node_b->next->next;
	}
	return (0);
}

