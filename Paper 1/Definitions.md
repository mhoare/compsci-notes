# Definitions

Useful definitions

| Name | Definition | Additional info |
| :----: | :---------- | :--------------- | 
| Heap | A pool of unused memory, used to allocate space for new data items | Allows more efficient use of memory when dealing with data of an unknown and changing size | 
| Stack Frame | The area where all parameters and local variables are stored until the end of the routine. | |
| Call stack | A special type of stack used to store information about active subroutines and functions. | The function is called and data passed to it. The return address is placed on the stack so that when the function is finished, it will look to the return address so it knows where to return to.<br/>The subroutine is running using local variables.<br />When a function is called, the current position is saved in the stack as a saved frame pointer. |
| Enqueue | Add an element to a queue | |
| Dequeue | Remove an element from a queue | |
