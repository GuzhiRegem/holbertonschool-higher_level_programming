#include "lists.h"

/**
 * get_at_idx - gets a index
 * @head: a
 * @idx: a
 * Return:a
 */
int get_at_idx(listint_t **head, int idx)
{
	int i = 0;
	listint_t *ite;

	ite = *head;
	while (i < idx)
	{
		ite = ite->next;
		i++;
	}
	return (ite->n);
}
/**
 * is_palindrome - check if is palindrome
 * @head: head of the list
 * Return: bool
 */
int is_palindrome(listint_t **head)
{
	listint_t *first;
	int lar, idx1, out = 1;

	first = *head;
	if (!first)
		return (1);
	lar = 0;
	while (first)
		first = first->next;
		lar++;
	for (idx1 = 0; idx1 < (lar / 2); idx1++)
	{
		if (get_at_idx(head, idx1) != get_at_idx(head, lar - idx1 - 1))
		{
			out = 0;
			break;
		}
	}
	return (out);
}
