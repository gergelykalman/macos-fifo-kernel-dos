# macos-fifo-kernel-dos
PoC of a macOS DoS that locks up the kernel

On macOS this results in a watchdog panic.


# Usage
Tune `n` and `size` to taste.


# Notes
I believe this has something to do with memory pressure when fifos have
unread data in them and the OOM killer fails to run properly, but I did
not investigate.

Since Apple does not consider DoS to be a security issue, full disclosure
is best.

