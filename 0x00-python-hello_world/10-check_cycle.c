#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 *check_cycle - Function checking if a singly LL has a cycle in it
 *@list: pointer to the singly linked list
 *
 *Return: 1 if there is a cycle and 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	tortoise = hare = list;

	while (tortoise != NULL && hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
		{
			return (1);
		}
	}

	return (0);
}
