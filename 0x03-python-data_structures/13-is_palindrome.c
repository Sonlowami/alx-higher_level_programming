#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - reverse a linked list
 * @head: the head of a linked list
 *
 * Return: pointer to the head of a linked list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *node_a, *node_b, *node_c;

	if (!head || !*head)
		return (NULL);
	node_a = *head;
	node_b = node_a->next;
	node_a->next = NULL;
	if (!node_b)
		return (node_a);
	node_c = node_b->next;
	while (node_b)
	{
		node_b->next = node_a;
		node_a = node_b;
		node_b = node_c;
		if (node_c)
			node_c = node_c->next;
	}
	*head = node_a;
	return (*head);
}
/**
 * is_palindrome - check if a linkedlist is a palindrome
 * @head: pointer to the reference to the first node of the list
 *
 * Return: 1 if palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *node, *reversed;

	if (!head || !*head || !(*head + 1))
		return (1);
	node = *head;
	reversed = reverse_list(head);
	while (node)
	{
		if (node->n != reversed->n)
			return (0);
		node = node->next, reversed = reversed->next;
	}
	return (1);
}
