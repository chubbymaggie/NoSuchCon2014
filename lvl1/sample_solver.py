#!/usr/bin/python2

from z3 import *
import struct

solution_str = "[ Synacktiv + NSC = <3 ]"
solutions = struct.unpack("<LLLLLL", solution_str)
N = len(solutions)

# Hook Z3's `>>` so it works with our algorithm
# (logical shift instead of arithmetic one)
BitVecRef.__rshift__  = LShR

pwd = [BitVec("pwd_%d" % i, 32) for i in range(N)]
pwd_orig = [pwd[i] for i in range(N)]
i = 0

pwd[i] = (pwd[i]+(- i))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+0x3ECA6F23)
pwd[i] = (pwd[i]+0x6EDC032)
pwd[i] = ((pwd[i] << 0x5)|(pwd[i] >> 0x1B))
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << 0x1D)|(pwd[i] >> 0x3))
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+0xD0358C15)
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << 0x10)|(pwd[i] >> 0x10))
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0xC)|(pwd[i] >> 0x14))
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = (pwd[i]+0x192B37D2)
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+i)
pwd[i] = ((pwd[i] << 0x9)|(pwd[i] >> 0x17))
pwd[i] = (pwd[i]^0x3D68A35C)
pwd[i] = (pwd[i]+0x73C69F47)
pwd[i] = (pwd[i]+0xDBFA3745)
pwd[i] = ((pwd[i] << 0x1C)|(pwd[i] >> 0x4))
pwd[i] = (pwd[i]+0x79662B5D)
pwd[i] = ((pwd[i] << 0xF)|(pwd[i] >> 0x11))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+0xD45CEF0A)
pwd[i] = (pwd[i]^0xA9BE160D)
pwd[i] = (pwd[i]+i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+0x3A2EE307)
pwd[i] = (pwd[i]+0xB65E867F)
pwd[i] = (pwd[i]^0xBFD991A0)
pwd[i] = ((pwd[i] << 0x1D)|(pwd[i] >> 0x3))
pwd[i] = (pwd[i]^i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]^0x4CC0DC26)
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]+0xD0970C74)
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]^0x7B4DE789)
pwd[i] = (pwd[i]^0x8103D046)
pwd[i] = (pwd[i]^0xCC4E5D94)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0x13)|(pwd[i] >> 0xD))
pwd[i] = (pwd[i]+0x81674F2B)
pwd[i] = ((pwd[i] << 0x14)|(pwd[i] >> 0xC))
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = (pwd[i]^i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]^0x38C1FEB8)
pwd[i] = (pwd[i]+i)
pwd[i] = ((pwd[i] << 0x1F)|(pwd[i] >> 0x1))
pwd[i] = ((pwd[i] << 0xD)|(pwd[i] >> 0x13))
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = ((pwd[i] << 0x6)|(pwd[i] >> 0x1A))
pwd[i] = ((pwd[i] << 0x5)|(pwd[i] >> 0x1B))
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = ((pwd[i] << 0x6)|(pwd[i] >> 0x1A))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+i)
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = ((pwd[i] << 0xB)|(pwd[i] >> 0x15))
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = (pwd[i]^i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << 0x18)|(pwd[i] >> 0x8))
pwd[i] = ((pwd[i] << 0x1E)|(pwd[i] >> 0x2))
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+0x87DD2BC5)
pwd[i] = (pwd[i]+0x737F298)
pwd[i] = ((pwd[i] << 0x17)|(pwd[i] >> 0x9))
pwd[i] = ((pwd[i] << 0x1C)|(pwd[i] >> 0x4))
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = ((pwd[i] << 0x1D)|(pwd[i] >> 0x3))
pwd[i] = (pwd[i]+i)
pwd[i] = ((pwd[i] << 0x12)|(pwd[i] >> 0xE))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0x1F)|(pwd[i] >> 0x1))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
i = (i+0x1)
pwd[i] = (pwd[i]^0x38C1FEB8)
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]+0xB65E867F)
pwd[i] = (pwd[i]^0xBFD991A0)
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = (pwd[i]+0x87DD2BC5)
pwd[i] = (pwd[i]+0x3ECA6F23)
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+0x737F298)
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = ((pwd[i] << 0x18)|(pwd[i] >> 0x8))
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << 0xF)|(pwd[i] >> 0x11))
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]^0x3D68A35C)
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]^i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << 0x5)|(pwd[i] >> 0x1B))
pwd[i] = ((pwd[i] << 0x5)|(pwd[i] >> 0x1B))
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]+i)
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = ((pwd[i] << 0x1D)|(pwd[i] >> 0x3))
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = (pwd[i]+0x79662B5D)
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = ((pwd[i] << 0xB)|(pwd[i] >> 0x15))
pwd[i] = ((pwd[i] << 0x6)|(pwd[i] >> 0x1A))
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << 0x6)|(pwd[i] >> 0x1A))
pwd[i] = (pwd[i]+i)
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = ((pwd[i] << 0x13)|(pwd[i] >> 0xD))
pwd[i] = ((pwd[i] << 0x12)|(pwd[i] >> 0xE))
pwd[i] = (pwd[i]+0x73C69F47)
pwd[i] = (pwd[i]^0x8103D046)
pwd[i] = (pwd[i]+i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+0x192B37D2)
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << 0x1F)|(pwd[i] >> 0x1))
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << 0x1E)|(pwd[i] >> 0x2))
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << 0xC)|(pwd[i] >> 0x14))
pwd[i] = (pwd[i]+0xD0358C15)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+0x81674F2B)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]^0x7B4DE789)
pwd[i] = (pwd[i]^i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]^0xA9BE160D)
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << 0x1D)|(pwd[i] >> 0x3))
pwd[i] = ((pwd[i] << 0xD)|(pwd[i] >> 0x13))
pwd[i] = (pwd[i]+i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << 0x14)|(pwd[i] >> 0xC))
pwd[i] = ((pwd[i] << 0x1F)|(pwd[i] >> 0x1))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+0x3A2EE307)
pwd[i] = (pwd[i]+0xDBFA3745)
pwd[i] = ((pwd[i] << 0x10)|(pwd[i] >> 0x10))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+i)
pwd[i] = ((pwd[i] << 0x9)|(pwd[i] >> 0x17))
pwd[i] = (pwd[i]+0xD45CEF0A)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << 0x17)|(pwd[i] >> 0x9))
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << 0x1C)|(pwd[i] >> 0x4))
pwd[i] = (pwd[i]+0x6EDC032)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+0xD0970C74)
pwd[i] = (pwd[i]^0xCC4E5D94)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+i)
pwd[i] = ((pwd[i] << 0x1D)|(pwd[i] >> 0x3))
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]^0x4CC0DC26)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0x1C)|(pwd[i] >> 0x4))
i = (i+0x1)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+0x73C69F47)
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]+0xD45CEF0A)
pwd[i] = (pwd[i]^0x38C1FEB8)
pwd[i] = (pwd[i]+0x737F298)
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << 0x9)|(pwd[i] >> 0x17))
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << 0x18)|(pwd[i] >> 0x8))
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = (pwd[i]^i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0x1D)|(pwd[i] >> 0x3))
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]^0x4CC0DC26)
pwd[i] = (pwd[i]^i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = ((pwd[i] << 0x1D)|(pwd[i] >> 0x3))
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << 0x1C)|(pwd[i] >> 0x4))
pwd[i] = ((pwd[i] << 0x1F)|(pwd[i] >> 0x1))
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]^0x8103D046)
pwd[i] = ((pwd[i] << 0x14)|(pwd[i] >> 0xC))
pwd[i] = ((pwd[i] << 0x17)|(pwd[i] >> 0x9))
pwd[i] = (pwd[i]+i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0x5)|(pwd[i] >> 0x1B))
pwd[i] = ((pwd[i] << 0x6)|(pwd[i] >> 0x1A))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0xF)|(pwd[i] >> 0x11))
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+i)
pwd[i] = ((pwd[i] << 0x13)|(pwd[i] >> 0xD))
pwd[i] = (pwd[i]^0xCC4E5D94)
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+0x6EDC032)
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]+0x3A2EE307)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << 0x1D)|(pwd[i] >> 0x3))
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << 0x1C)|(pwd[i] >> 0x4))
pwd[i] = ((pwd[i] << 0x1F)|(pwd[i] >> 0x1))
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+0x81674F2B)
pwd[i] = (pwd[i]+0xD0358C15)
pwd[i] = ((pwd[i] << 0x10)|(pwd[i] >> 0x10))
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0x1E)|(pwd[i] >> 0x2))
pwd[i] = (pwd[i]+i)
pwd[i] = ((pwd[i] << 0x6)|(pwd[i] >> 0x1A))
pwd[i] = ((pwd[i] << 0x12)|(pwd[i] >> 0xE))
pwd[i] = (pwd[i]+i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = (pwd[i]+0x192B37D2)
pwd[i] = (pwd[i]+i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0x5)|(pwd[i] >> 0x1B))
pwd[i] = (pwd[i]+0x87DD2BC5)
pwd[i] = ((pwd[i] << 0xB)|(pwd[i] >> 0x15))
pwd[i] = (pwd[i]+0xD0970C74)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+0x79662B5D)
pwd[i] = ((pwd[i] << 0xC)|(pwd[i] >> 0x14))
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = (pwd[i]+0xDBFA3745)
pwd[i] = (pwd[i]^0x3D68A35C)
pwd[i] = (pwd[i]+0xB65E867F)
pwd[i] = (pwd[i]+0x3ECA6F23)
pwd[i] = ((pwd[i] << 0xD)|(pwd[i] >> 0x13))
pwd[i] = (pwd[i]^0xBFD991A0)
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]^0xA9BE160D)
pwd[i] = (pwd[i]^0x7B4DE789)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
i = (i+0x1)
pwd[i] = (pwd[i]+0x192B37D2)
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]^0xBFD991A0)
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = ((pwd[i] << 0xC)|(pwd[i] >> 0x14))
pwd[i] = (pwd[i]+i)
pwd[i] = ((pwd[i] << 0x1C)|(pwd[i] >> 0x4))
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = ((pwd[i] << 0x10)|(pwd[i] >> 0x10))
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << 0x13)|(pwd[i] >> 0xD))
pwd[i] = (pwd[i]+0xD0358C15)
pwd[i] = ((pwd[i] << 0x1D)|(pwd[i] >> 0x3))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0x18)|(pwd[i] >> 0x8))
pwd[i] = (pwd[i]+i)
pwd[i] = ((pwd[i] << 0x1D)|(pwd[i] >> 0x3))
pwd[i] = (pwd[i]+0x3A2EE307)
pwd[i] = (pwd[i]^0x38C1FEB8)
pwd[i] = ((pwd[i] << 0x6)|(pwd[i] >> 0x1A))
pwd[i] = ((pwd[i] << 0xB)|(pwd[i] >> 0x15))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+0x87DD2BC5)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0x1F)|(pwd[i] >> 0x1))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0x5)|(pwd[i] >> 0x1B))
pwd[i] = ((pwd[i] << 0x1F)|(pwd[i] >> 0x1))
pwd[i] = (pwd[i]+0x73C69F47)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]+0xB65E867F)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+0x737F298)
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = ((pwd[i] << 0x17)|(pwd[i] >> 0x9))
pwd[i] = (pwd[i]^0xA9BE160D)
pwd[i] = ((pwd[i] << 0x5)|(pwd[i] >> 0x1B))
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << 0xD)|(pwd[i] >> 0x13))
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0x1C)|(pwd[i] >> 0x4))
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+0x81674F2B)
pwd[i] = (pwd[i]^0x7B4DE789)
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = (pwd[i]^0x3D68A35C)
pwd[i] = (pwd[i]+0x6EDC032)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]^0xCC4E5D94)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]+i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0x6)|(pwd[i] >> 0x1A))
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << 0x12)|(pwd[i] >> 0xE))
pwd[i] = ((pwd[i] << 0x9)|(pwd[i] >> 0x17))
pwd[i] = (pwd[i]+0x3ECA6F23)
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = (pwd[i]^0x8103D046)
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << 0xF)|(pwd[i] >> 0x11))
pwd[i] = (pwd[i]+0xD0970C74)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+0x79662B5D)
pwd[i] = ((pwd[i] << 0x14)|(pwd[i] >> 0xC))
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << 0x1E)|(pwd[i] >> 0x2))
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = (pwd[i]+0xDBFA3745)
pwd[i] = (pwd[i]+0xD45CEF0A)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]^0x4CC0DC26)
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << 0x1D)|(pwd[i] >> 0x3))
i = (i+0x1)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << 0x18)|(pwd[i] >> 0x8))
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]+0xD0970C74)
pwd[i] = (pwd[i]+0x192B37D2)
pwd[i] = ((pwd[i] << 0x1F)|(pwd[i] >> 0x1))
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = (pwd[i]^0x38C1FEB8)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]^i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0x1F)|(pwd[i] >> 0x1))
pwd[i] = (pwd[i]+i)
pwd[i] = ((pwd[i] << 0xD)|(pwd[i] >> 0x13))
pwd[i] = (pwd[i]+0x737F298)
pwd[i] = (pwd[i]+i)
pwd[i] = ((pwd[i] << 0x17)|(pwd[i] >> 0x9))
pwd[i] = (pwd[i]+0x79662B5D)
pwd[i] = (pwd[i]^0xA9BE160D)
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = ((pwd[i] << 0x5)|(pwd[i] >> 0x1B))
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = ((pwd[i] << 0x12)|(pwd[i] >> 0xE))
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = (pwd[i]+0xDBFA3745)
pwd[i] = ((pwd[i] << 0x13)|(pwd[i] >> 0xD))
pwd[i] = ((pwd[i] << 0x9)|(pwd[i] >> 0x17))
pwd[i] = ((pwd[i] << 0x1C)|(pwd[i] >> 0x4))
pwd[i] = (pwd[i]+0x81674F2B)
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+0xB65E867F)
pwd[i] = (pwd[i]^0xBFD991A0)
pwd[i] = (pwd[i]+0x6EDC032)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]+i)
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+0x73C69F47)
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0x6)|(pwd[i] >> 0x1A))
pwd[i] = ((pwd[i] << 0x5)|(pwd[i] >> 0x1B))
pwd[i] = ((pwd[i] << 0x1D)|(pwd[i] >> 0x3))
pwd[i] = ((pwd[i] << 0xB)|(pwd[i] >> 0x15))
pwd[i] = ((pwd[i] << 0x10)|(pwd[i] >> 0x10))
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+0x87DD2BC5)
pwd[i] = (pwd[i]+0x3A2EE307)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]^i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << 0x1D)|(pwd[i] >> 0x3))
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << 0x6)|(pwd[i] >> 0x1A))
pwd[i] = ((pwd[i] << 0x1D)|(pwd[i] >> 0x3))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0x14)|(pwd[i] >> 0xC))
pwd[i] = (pwd[i]^0xCC4E5D94)
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]^0x4CC0DC26)
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << 0xF)|(pwd[i] >> 0x11))
pwd[i] = (pwd[i]+0xD45CEF0A)
pwd[i] = ((pwd[i] << 0xC)|(pwd[i] >> 0x14))
pwd[i] = ((pwd[i] << 0x1E)|(pwd[i] >> 0x2))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]^0x7B4DE789)
pwd[i] = (pwd[i]+0x3ECA6F23)
pwd[i] = (pwd[i]^0x3D68A35C)
pwd[i] = (pwd[i]+0xD0358C15)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]^0x8103D046)
pwd[i] = ((pwd[i] << 0x1C)|(pwd[i] >> 0x4))
pwd[i] = (pwd[i]^i)
i = (i+0x1)
pwd[i] = (pwd[i]+0xD0358C15)
pwd[i] = (pwd[i]+0x6EDC032)
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << 0x6)|(pwd[i] >> 0x1A))
pwd[i] = ((pwd[i] << 0x6)|(pwd[i] >> 0x1A))
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]^0xBFD991A0)
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << 0x9)|(pwd[i] >> 0x17))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0x1C)|(pwd[i] >> 0x4))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << 0x1D)|(pwd[i] >> 0x3))
pwd[i] = ((pwd[i] << 0x5)|(pwd[i] >> 0x1B))
pwd[i] = (pwd[i]+i)
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]^i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0x12)|(pwd[i] >> 0xE))
pwd[i] = (pwd[i]+0x3ECA6F23)
pwd[i] = (pwd[i]^0x8103D046)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+i)
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+i)
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]+0x737F298)
pwd[i] = ((pwd[i] << 0x1E)|(pwd[i] >> 0x2))
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << 0x1F)|(pwd[i] >> 0x1))
pwd[i] = (pwd[i]+0xD0970C74)
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((pwd[i] << 0x10)|(pwd[i] >> 0x10))
pwd[i] = (pwd[i]^0xCC4E5D94)
pwd[i] = (pwd[i]+0x73C69F47)
pwd[i] = (pwd[i]^0x4CC0DC26)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]^0x7B4DE789)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+0xD45CEF0A)
pwd[i] = (pwd[i]+0x79662B5D)
pwd[i] = (pwd[i]+0x81674F2B)
pwd[i] = (pwd[i]^0x38C1FEB8)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0x1D)|(pwd[i] >> 0x3))
pwd[i] = (pwd[i]+0x87DD2BC5)
pwd[i] = ((pwd[i] << 0xB)|(pwd[i] >> 0x15))
pwd[i] = (pwd[i]^i)
pwd[i] = ((pwd[i] << 0x17)|(pwd[i] >> 0x9))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]+(- i))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << 0x5)|(pwd[i] >> 0x1B))
pwd[i] = ((pwd[i] << 0x1C)|(pwd[i] >> 0x4))
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = (pwd[i]+i)
pwd[i] = (pwd[i]+0xDBFA3745)
pwd[i] = (pwd[i]+0x3A2EE307)
pwd[i] = (pwd[i]^i)
pwd[i] = (pwd[i]^0x3D68A35C)
pwd[i] = ((pwd[i] << 0x1D)|(pwd[i] >> 0x3))
pwd[i] = (pwd[i]+0x192B37D2)
pwd[i] = ((pwd[i] << 0xF)|(pwd[i] >> 0x11))
pwd[i] = (pwd[i]+(- i))
pwd[i] = (pwd[i]+0xB65E867F)
pwd[i] = ((pwd[i] << 0xD)|(pwd[i] >> 0x13))
pwd[i] = ((pwd[i] << 0x18)|(pwd[i] >> 0x8))
pwd[i] = (pwd[i]^0xA9BE160D)
pwd[i] = (pwd[i]^i)
pwd[i] = ((0x0|pwd[i])^0xFFFFFFFF)
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
pwd[i] = ((pwd[i] << 0x1F)|(pwd[i] >> 0x1))
pwd[i] = ((pwd[i] << 0x13)|(pwd[i] >> 0xD))
pwd[i] = ((pwd[i] << ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F))|(pwd[i] >> ((i+0x1)&0x1F)))
pwd[i] = ((pwd[i] << 0xC)|(pwd[i] >> 0x14))
pwd[i] = ((pwd[i] << 0x14)|(pwd[i] >> 0xC))
pwd[i] = ((pwd[i] << ((i+0x1)&0x1F))|(pwd[i] >> ((((0x0|i)^0xFFFFFFFF)+0x20)&0x1F)))
i = (i+0x1)

s = Solver()

for i in range(N):
    s.add(pwd[i] == solutions[i])

assert s.check() == sat

m = s.model()
sol_dw = [m[pwd_orig[i]].as_long() for i in range(N)]
key = ''.join(("%08x" % dw)[::-1].upper() for dw in sol_dw)

print "KEY = %s" % key
