#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a number into a sorted singly linked list
 * @head: pointer to address of head node
 * @number: number to be added into sorted list
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (*head)
	{
		tmp = *head;
		if (number <= tmp->n)
		{
			new->next = tmp;
			*head = new;
		}
		else
		{
			while (number > (tmp->next)->n)
			{
				tmp = tmp->next;
				if (!tmp->next)
					break;
			}
			new->next = tmp->next;
			tmp->next = new;
		}
	}
	else
	{
		new->next = NULL;
		*head = new;
	}
	return (new);
}
