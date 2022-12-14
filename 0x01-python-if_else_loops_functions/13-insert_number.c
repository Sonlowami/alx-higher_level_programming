#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - insert a node in a sorted singly linked_list
 * @head: pointer to refrerence to first node in the list
 * @number: the number contained in n field of the node
 *
 * Return: pointer to the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node_a, *node_b, *temp;

	if (!*head)
	{
		node_a = malloc(sizeof(listint_t *));
		node_a->n = number;
		node_a->next = NULL;
		*head = node_a;
		return (node_a);
	}
	node_a = *head, node_b = malloc(sizeof(*head));
	if (!node_b)
		return (NULL);
	node_b->n = number, node_b->next = NULL;
	if (node_a->n > node_b->n)
	{
		node_b->next = node_a;
		*head = node_b;
		return (node_b);
	}
	while (node_a)
	{
		if (!node_a->next)
		{
			node_a->next = node_b;
			break;
		}
		if (node_a->n < node_b->n)
		{
			temp = node_a;
			node_a = node_a->next;
		}
		else
		{
			node_b->next = node_a;
			temp->next = node_b;
			break;
		}
	}
	return (node_b);
}

