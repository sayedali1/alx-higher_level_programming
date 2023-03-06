#include "lists.h"
/**
 * check_cycle - fun that check if list is cycle or not
 * @list: list of type listint_t
 * Return: 1 if cycle , 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *node = list;
	listint_t *node2 = list;

	if (!list)
	{
		return (0);
	}

		for (; node != NULL && node2 != NULL;)
		{
			node = node->next->next;
			node2 = node2->next;

			if (node == node2)
				return (1);
		}
		return (0);
}

