#include "lists.h"
#include<stdio.h>
/**
 * list_len - fun that get the len of a list
 * @head:pointer the first element of a list
 * Return: len of the list
 */
int list_len(listint_t *head)
{
	listint_t *temp = head;
	int i;

	for (i = 1; temp->next != NULL; i++)
		temp = temp->next;
	return (i);
}

/**
 * reverse_listint - fun that reverse linked list
 * @head: pointer to the first node of linked list
 * Return: pointer to the header
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev, *next;

	prev = NULL;

	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;

	return (*head);
}

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head, *first_half = NULL, *sec_half = NULL, *temp2 = NULL;
	int i, len;

	if (*head == NULL)
		return (1);
	len = list_len(*head);
	if (len == 1)
		return (1);
	if (len % 2 != 0) /* if not even list */
		return (0);
	temp = *head;
	for (i = 1; i <= len; i++)
	{
		if (i <= len / 2) /* add the first half of the main list */
			add_nodeint_end(&first_half, temp->n);
		else /* add the sec half */
			add_nodeint_end(&sec_half, temp->n);
		temp = temp->next;
	}
	reverse_listint(&sec_half); /* reverse the sec list */

	/* check if the first list equal the sec list */
	temp = first_half;
	temp2 = sec_half;
	for (i = 0; i < list_len(first_half); i++)
	{
		if (temp->n != temp2->n)
			return (0);
		temp = temp->next;
		temp2 = temp2->next;
	}
	free_listint(first_half);
	free_listint(sec_half);

	return (1);
}
