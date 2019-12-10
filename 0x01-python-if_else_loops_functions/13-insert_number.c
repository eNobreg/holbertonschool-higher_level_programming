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
	listint_t *current = NULL;

	if (new == NULL)
		return (NULL);
	new->n = number, current = *head;
	if (*head == NULL)
	{
		new->next = NULL, *head = new;
		return (*head);
	}
	if (number < current->n)
	{
		new->next = *head, *head = new;
		return (new);
	}
	while (current)
	{
		if (current->next)
		{
			if (number < current->next->n)
			{
				new->next = current->next;
				current->next = new;
				if (new == NULL)
					return (NULL);
				return (new);
			}
		}
		else
			if (current->next == NULL)
			{
				current->next = new;
				return (new);
			}
		current = current->next;
	}
	free(new);
	return (NULL);
}
