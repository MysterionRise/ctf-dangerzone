How to. Since random_shuffle isn't using random generator by default we could predict the output from the server

```nc challs.n00bzunit3d.xyz 10402
0123456789
4378052169
0578439216
5763842019
4602813957
4051796283
3856172409
```

next run will get exactly the same (purely based on positions)

Just manually send the string, see shuffling and redo that
```
nc challs.n00bzunit3d.xyz 10402
587216934q
123456789q
n00bz{5up3r_dup3r_ultr4_54f3_p455w0rd_c9da1fffa738}
```