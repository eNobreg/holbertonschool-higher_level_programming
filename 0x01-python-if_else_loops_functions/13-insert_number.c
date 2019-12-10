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

	current = *head;

	while (current)
	{
		if (number < current->next->n)
		{
			new->n = number;
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	free(new);
	return (NULL);
}
