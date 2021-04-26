# truth-table-generator
Truth table generator written in Python. Uses Shunting-Yard algorithm to parse logical expressions with `AND`, `OR`, `NOT`, and `IMPLIES` operators, and parentheses.

## Usage

Arguments: `latex`, `short`. 
 - `latex`: specifies whether or not to print as LaTeX source
 - `short`: specifies whether or not to, when printing LaTeX source, use T/F instead of True/False

### Example: no arguments

```
$ python table_generator.py
Enter variable names separated by spaces: P Q
Enter a logical expression of your variables: P AND Q
Enter another expression or hit <Return> to proceed:
        P       Q       P AND Q
        True    True    True
        True    False   False
        False   True    False
        False   False   False
```

### Example: `latex` argument

```
$ python table_generator.py latex
Enter variable names separated by spaces: P Q
Enter a logical expression of your variables: P AND Q
Enter another expression or hit <Return> to proceed:
\begin{array}{c|c|c}
 P & Q & P \land Q\\
 \hline
 \text{True} & \text{True} & \text{True}\\
 \text{True} & \text{False} & \text{False}\\
 \text{False} & \text{True} & \text{False}\\
 \text{False} & \text{False} & \text{False}\\
\end{array}
```

LaTeX render:

![](latex_render_1.png)

### Example: `latex` and `short` arguments:

```
$ python table_generator.py latex short
Enter variable names separated by spaces: P Q
Enter a logical expression of your variables: P AND Q
Enter another expression or hit <Return> to proceed:
\begin{array}{c|c|c}
 P & Q & P \land Q\\
 \hline
 \text{T} & \text{T} & \text{T}\\
 \text{T} & \text{F} & \text{F}\\
 \text{F} & \text{T} & \text{F}\\
 \text{F} & \text{F} & \text{F}\\
\end{array}
```

LaTeX render:

![](latex_render_2.png)
