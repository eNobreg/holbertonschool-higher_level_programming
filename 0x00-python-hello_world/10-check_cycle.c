#include "lists.h"
/**
 * check_cycle - Checks a linked list for a cycle
 * @list: The list to check
 * Return: 0 or 1 based on the cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast && slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);

}
