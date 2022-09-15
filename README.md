# SSW-567-WS

<img width="1194" alt="Screen Shot 2022-09-14 at 9 21 30 PM" src="https://user-images.githubusercontent.com/42434419/190292536-a6b631e7-f773-493a-82e4-fe316417474e.png">

<img width="1188" alt="Screen Shot 2022-09-14 at 9 22 01 PM" src="https://user-images.githubusercontent.com/42434419/190292571-a2c4da81-7cee-4918-b9f1-1b2f7ad10272.png">

One challenge I encountered while completing this assignment is a rounding error with floating point numbers. For example, the triangle (5, 5, 5 * sqrt(2)) should be an isosceles right triangle. However, this causes a bug in the classification function because python thinks 5 * sqrt(2) is 50.00000000000001 instead of 50.

The requirements specification for this assignment was intuitive, but incomplete. The specification goes into the properties of each triangle, however, I had to do extra research to find that if the sum of the 2 smaller sides is less than the third side, the 3 lengths do not make a complete triangle.

The only challenge I encountered with Python and the UnitTest class was finding how to run the test functions automatically when running the script instead of manually running the tests. I also found that when one test case within a test function fails, the whole function counts as a fail. This confused me because there could be 3 tests in a function that fail, but the output only says there was 1 failure (refers to the function instead).

I knew I was done with the assignment when there was a test case for each kind of input. There were many test cases for an invalid input because I considered inputs that weren't integers or floats. As for the valid inputs, I knew there were enough test cases when there was 1 test case for each type of triangle.
