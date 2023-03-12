#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - check if a list is palindrome
 * @head: pointer to head of singly linked list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	unsigned int len = 0, i = 0;
	int *data;

	if (head == NULL)
		return (0);
	if (*head == NULL) /* empty list is palindrome */
		return (1);

	while (temp) /* find size of linked list */
	{
		temp = temp->next;
		len++;
	}
	if (len == 1) /* single node list is palindrome */
		return (1);

	data = malloc(sizeof(int) * len);
	temp = *head;

	while (temp) /* add list to into array */
	{
		data[i++] = temp->n;
		temp = temp->next;
	}

	for (i = 0; i <= (len / 2); i++)
	{
		if (data[i] != data[len - i - 1])
		{
			free(data);
			return (0);
		}
	}
	free(data);
	return (1);
}
