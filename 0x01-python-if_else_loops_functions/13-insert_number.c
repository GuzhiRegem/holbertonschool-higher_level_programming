#include "lists.h"

/**
 *insert_node  - inserts a node at the beggining of the list
 *@head: head of the list
 *@number: number
 *Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *out = NULL;
	listint_t *behind = NULL, *after;

	if (!head)
		return (out);
	after = *head;
	while (after)
	{
		if (after->n <= number)
			break;
		behind = after;
		after = after->next;
	}
	out = malloc(sizeof(listint_t));
	if (!out)
		return (out);
	out->n = number;
	out->next = after;
	if (behind)
		behind->next = out;
	return (out);
}
