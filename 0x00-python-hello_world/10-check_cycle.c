#include "lists.h"
/**
 * check_cycle - check if a linkedlist loops
 * @list: pointer to the head of the list
 *
 * Return: 1 if found, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	int i, j;
	listint_t *node_a, *node_b, **used;

	used = malloc(sizeof(list) * 64);
	if (!used)
		exit(-1);
	node_a = list, i = 0;
	while (node_a)
	{
		used[i] = node_a;
		node_b = node_a->next;
		for (j = 0; used[j]; j++)
		{
			if (node_b == used[j])
			{
				free(used);
				return (1);
			}
		}
		node_a = node_b;
	}
	free(used);
	return (0);
}

