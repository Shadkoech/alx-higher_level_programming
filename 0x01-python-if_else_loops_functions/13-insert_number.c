#include "lists.h"
#include <stddef.h>
#include <stdlib.h>


/**
 *insert_node - Function that inserts a number into a sorted LL
 *@head: a double pointer to the first node on the LL
 *@number: the number to insert into a LL
 *
 *Return: Address of the newnode, NULL otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *prev, *newnode;

	temp = (*head);
	prev = NULL;

	newnode = malloc(sizeof(newnode));
	if (newnode == NULL)
	{
		return (NULL);
	}

	newnode->n = number;
	newnode->next = NULL;

	while (temp != NULL && temp->n < number)
	{
		prev = temp;
		temp = temp->next;
	}

	if (prev == NULL)
	{
		newnode->next = (*head);
		(*head) = newnode;
	}
	else
	{
		prev->next = newnode;
		newnode->next = temp;
	}

	return (newnode);
}
