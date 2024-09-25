```
strings structured_annuity.dump | grep PCTF
```

Unfortunately, not found anything

Always try to grep for reversed flag as well, e.g.

```
strings structured_annuity.dump | grep FTCP
```

```
strings structured_annuity.dump | grep FTCP      
}W0N_H5@C_D33N_I_7U8{FTCP ohce
}W0N_H5@C_D33N_I_7U8{FTCP
```

We could use `| rev`

```
strings structured_annuity.dump | rev | grep PCTF
echo PCTF{8U7_I_N33D_C@5H_N0W}
PCTF{8U7_I_N33D_C@5H_N0W}
```