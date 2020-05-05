# Embroidery

## Story

Winter is coming, so does Christmas. You have a small enterprise
that produces Christmas tree decoration. This year you bought
a machine that is able to produce [embroidery](https://www.embroiderypanda.com/image/cache/data/A-A9933/Ornate-Christmas-Tree-Filled-Machine-Embroidery-Design-Digitized-Pattern-700x700.jpg)
and is controllable through a programmable interface.

The machine requests a matrix as an input where `0`
means an empty pixel, and positive integers mean different
colors.

Your job is to design simple ornament matrices for
this year's Christmas fair.

## What are you going to learn?

You'll have to:
 - think in algorithms,
 - handle edge cases,
 - use parameters and default arguments,
 - use nested lists and advanced list manipulation.

## Tasks


1. Implement the `draw_rectangle(width, height)` function to return matrices like this:
    ```
    1 1 1 1 1 1 1          1 1 1 1 1 1 1          1 1 1 1 1 1 1
    1 1 1 1 1 1 1          1 2 2 2 2 2 1          1 1 1 1 1 1 1
    1 1 1 1 1 1 1          1 2 2 2 2 2 1          1 1 2 2 2 1 1
    1 1 1 1 1 1 1          1 2 2 2 2 2 1          1 1 2 2 2 1 1
    1 1 1 1 1 1 1          1 2 2 2 2 2 1          1 1 1 1 1 1 1
    1 1 1 1 1 1 1          1 1 1 1 1 1 1          1 1 1 1 1 1 1
    ```

    - There are further optional parameters, `border_color`, `fill_color`, and `border_width`, all with default values of `1`.
    - Called with default arguments, the returned matrix is a `width`-by-`height` rectangle shape marked by `1`s.
    - The rectangle's border has `border_color`, and it is filled with `fill_color`.
    - The third optional parameter, `border_width`, specifies the width of the border.
    - There are no completely empty rows or columns in the returned matrix.
    - The function provides reasonable answers to edge cases (all combinations of integers as parameters).

2. Implement the `draw_triangle(height)` function to return arrays like this:
    ```
    0 0 0 1 0 0 0          0 0 0 1 0 0 0
    0 0 1 1 1 0 0          0 0 1 2 1 0 0
    0 1 1 1 1 1 0          0 1 2 2 2 1 0
    1 1 1 1 1 1 1          1 1 1 1 1 1 1
    ```

    - There are further optional parameters, `border_color` and `fill_color`, all with default values of `1`.
    - Called with default arguments, the returned matrix consists of `height` rows and shows a tringle filled with `1`s.
    - The triangle's border has `border_color`, and it is filled with `fill_color`.
    - There are no completely empty rows or columns in the returned matrix.
    - The function provides reasonable answers to edge cases (all combinations of integers as parameters).

3. Implement the `draw_christmas_tree(blocks)` function to return arrays like this (when `blocks == 4`):
    ```
    0 0 0 0 0 1 0 0 0 0 0
    0 0 0 0 1 2 1 0 0 0 0
    0 0 0 1 2 2 2 1 0 0 0
    0 0 0 0 1 2 1 0 0 0 0
    0 0 0 1 2 2 2 1 0 0 0
    0 0 1 2 2 2 2 2 1 0 0
    0 0 0 1 2 2 2 1 0 0 0
    0 0 1 2 2 2 2 2 1 0 0
    0 1 2 2 2 2 2 2 2 1 0
    0 0 1 2 2 2 2 2 1 0 0
    0 1 2 2 2 2 2 2 2 1 0
    1 1 1 1 1 1 1 1 1 1 1
    ```

    - There are further optional parameters, `border_color` and `fill_color`, all with default values of `1`.
    - Called with default arguments, the returned matrix shows a Christmas tree made of `blocks` pieces of trapezoid blocks and filled with `1`s. Each block has 3 rows, and each first row is one step shorter than the last row of the block above.
    - The triangle's border has `border_color`, and it is filled with `fill_color`.
    - There are no completely empty rows or columns in the returned matrix.
    - The function provides reasonable answers to edge cases (all combinations of integers as parameters).

4. [OPTIONAL] Implement the `draw_circle(radius)` function to return arrays like this (truncated):
    ```
    0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 1 1 1 2 2 2 2 2 2 2 1 1 1 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 1 1 0 0 0 0 0 0 0
    0 0 0 0 0 0 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 0 0 0 0 0 0
    0 0 0 0 0 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 0 0 0 0 0
    0 0 0 0 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 0 0 0 0
    0 0 0 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 0 0 0
    0 0 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 0 0
    0 0 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 0 0
    0 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 0
    0 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 0
    0 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 0
    1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1
    1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1
    1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1
    ```

    - There are further optional parameters, `border_color` and `fill_color`, all with default values of `1`.
    - Called with default arguments, the returned matrix shows a circle of radius `r` filled with `1`s.
    - The returned matrix shows a continuous circle outline of `border_color`, and filled with `fill_color`.
    - There are no completely empty rows or columns in the returned matrix.
    - The function provides reasonable answers to edge cases (all combinations of integers as parameters).


## General requirements


None

## Hints

- Try to solve the problems without distinguishing border and the inside first
  (i.e. `border_color == fill_color`), you may find them much easier this way.
- This is especially true for the `draw_circle` function.
  Drawing a nice border for a circle is a rather advanced exercise,
  even though the only extra math needed for the solution
  is the Pythagorean theorem to calculate distance.

## Starting repository

> **For your information**: Unfortunately, GitHub Classroom has an unstable service regarding repository creation and imports. If your repository fails to create or there are issues with code imports you can do the following steps:
>
> 1. Wait. Sometimes it gets done after 1-2 hours.
> 2. Write to your mentors to do it manually for you.
>
> In the meantime, we are working on an own solution to replace GitHub Classroom. We plan to have it in the first quarter of 2020.


Click here to clone your own Git repository:
https://classroom.github.com/a/obBDAwez

## Background materials

- :exclamation: [Nested lists](https://learn.code.cool/full-stack/#/../pages/notebooks/nested-lists.html)
- :exclamation: [On default arguments](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions) in the documentation

## Acceptance review

You will need this only at review time, **after** completing the project.
[Use this form](https://forms.gle/ittx2DLWQwKTtxvq9) to record the review you provide for your peer.