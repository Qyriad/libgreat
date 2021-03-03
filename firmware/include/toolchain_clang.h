/*
 * This file is part of libgreat
 *
 * Toolchain helper functions.
 */

#ifndef __LIBGREAT_TOOLCHAIN_COMPILER_H__
#define __LIBGREAT_TOOLCHAIN_COMPILER_H__

#ifndef PRIu32

#define PRIu8  "hhu"
#define PRIu16 "hu"
#define PRIu32 "lu"
#define PRIu64 "llu"

#define PRId8  "hhd"
#define PRId16 "hd"
#define PRId32 "ld"
#define PRId64 "lld"

#define PRIi8  "hhi"
#define PRIi16 "hi"
#define PRIi32 "li"
#define PRIi64 "lli"

#define PRIx8  "hhx"
#define PRIx16 "hx"
#define PRIx32 "lx"
#define PRIx64 "llx"

#define PRIX8  "hhX"
#define PRIX16 "hX"
#define PRIX32 "lX"
#define PRIX64 "llX"

#define PRIo8  "hho"
#define PRIo16 "ho"
#define PRIo32 "lo"
#define PRIo64 "llo"

#endif

#endif
