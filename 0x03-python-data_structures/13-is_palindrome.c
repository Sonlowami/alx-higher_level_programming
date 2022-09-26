#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - check if a linkedlist is a palindrome
 * @head: pointer to the reference to the first node of the list
 *
 * Return: 1 if palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	int len, i, x[1024];
	listint_t *node;

	if (!head || !*head || !(*head + 1))
		return (1);
	node = *head, len = i = 0;
	while (node)
	{
		x[len++] = node->n;
		node = node->next;
	}
	len--;
	for (; i < len; i++, len--)
	{
		if (x[i] != x[len])
			return (0);
	}
	return (1);
}
