#!/usr/bin/env lua5.1

socket = require("socket")
local http = require("socket.http")
local body, code = http.request("http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test")
if not body then error(code) end

local f = assert(io.open('test.log', 'wb'))
f:write(body)
f:close()
