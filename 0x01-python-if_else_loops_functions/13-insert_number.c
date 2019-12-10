#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node-  inserts a node
 * @head: Address of the node of the singly linked list
 * @number: data to insert
 * Return: A pointer to new
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *current;

	if (new == NULL)
		return (NULL);
	if (*head == NULL)
		*head = new;

	current = *head;

	if (number < current->n)
	{
		new->next = *head;
		new->n = number;
		*head = new;
		return (new);
	}
	while (current)
	{
		if (number < current->next->n)
		{
			new->n = number;
			new->next = current->next;
			current->next = new;
			if (new == NULL)
				return (NULL);
			return (new);
		}
		current = current->next;
	}
	free(new);
	return (NULL);
}
