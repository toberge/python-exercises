# RSA cracking

## A description of how you approached the problem.
Having learned about and practiced RSA cryptography in last semester's maths course,
I had no need to read much about RSA before solving this problem.

In a rather simpleminded way, I tried using the decrypt() function in the supplied code
to run a brute-force attack on the encrypted text.
Relatively quickly I found the solution 14599 and considered myself done,
only bothering to run a larger test range today because I felt like doing a little more.

## What are the problems with this simple implementation of RSA?

Firstly, the prime number generation will take a ridiculous amount of time
for large n, since the complexity is something like O(N!)
\- where N is the amount of numbers checked.

Secondly, and in part because of the above, the prime numbers will not be that large.
Extending the restriction of n=100 primes in the pool would alleviate the problem only slightly,
since the implementation simply finds two random numbers that are not equal and uses them in generating the keypair,
meaning the numbers could very well be rather small.

## Did you find multiple solutions? Explain.
Running my brute force code from 1 to 99,999, I found two actual solutions:
**p = 14599 and 64327** both gave the correct plaintext

I also found three other "solutions" that at least started with an h:  
**p = 31175** gave h堦堦psⰓ녔녔鸿𖘺𗉁wi𒿘ip鸿֧i𑫂𗉁oֵg녔wi𒿘i녔R惊褏_员ֵ儧p堦os儧s堦鸿𘉉)䧍褏堦堦𑫂𒿘s_𑫂g𑫂i𖘺s堦_pl𑫂i𖘺_R惊褏  
**p = 47751** gave h摭摭ps莺莺㢅𔮫wi𒎑ip㢅틜i𔨝𔮫o멜g莺wi𒎑i莺R镨貑_𖴳멜抱p摭os抱s摭㢅춢)𐀵貑摭摭𔨝𖴳𒎑s_𔨝g𔨝is摭_pl𔨝i_R镨貑  
**p = 80903** gave h堦堦psⰓ녔녔鸿𖘺𗉁wi𒿘ip鸿֧i𑫂𗉁oֵg녔wi𒿘i녔R惊褏_员ֵ儧p堦os儧s堦鸿𘉉)䧍褏堦堦𑫂𒿘s_𑫂g𑫂i𖘺s堦_pl𑫂i𖘺_R惊褏  
- which is utter gibberish of too-high Unicode values and obviously not the intended message.

At this point the code takes a signifcant amount of time to run, though,
so going past a hundred thousand is outside my scope.
