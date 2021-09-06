#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *rabbit = list;
	listint_t *turtle_n = NULL;
	listint_t *rabbit_n = NULL;
	int found = 0;

	while(1)
	{
		turtle_n = turtle->next;
		rabbit_n = rabbit->next;
		if (rabbit_n == turtle)
			found = 1;
		if (!turtle_n || !rabbit_n || found || !rabbit_n->next)
			break;
		turtle = turtle_n;
		rabbit = rabbit_n->next;
	}
	return(found);
}
