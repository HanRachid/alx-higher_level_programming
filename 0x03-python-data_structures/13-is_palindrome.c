#include "lists.h"
#include <string.h>
#include <stdio.h>
/**
 * is_palindrome - checks if array of int is palindrom
 * @head: struct for linked list
 *
 * Return: 1 if palindrom, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t **feet = head;
	int headsize = 0;
	listint_t *currentfeet = *feet;
	listint_t *currenthead = *head;
	int arr[sizeof(head)];

	while (currentfeet != NULL)
	{
		arr[headsize] = currentfeet->n;
		currentfeet = currentfeet->next;
		headsize++;
	}
	headsize--;
	while (headsize != 0)
	{
		if (arr[headsize] != currenthead->n)
			return (0);

		headsize--;
		currenthead = currenthead->next;
	}
	return (1);
}
