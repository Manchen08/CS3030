#!/usr/bin/env lua5.3
import sys

local function printDigit(d)
    print(d)

local function printBarCode(zipCode)
    code = []
    check = 0
    for i,v in in ipairs(zipCode) do
        check = check + v
	end
	
    if check % 10 == 0 then
        zipCode += "0"

    else
        for x=1,9 do
            check = check + x
            if(check % 10 == 0):
                check = x
                break
		end
		
        zipCode = zipCode..check

		print(check)
		print(zipCode)
	end

    for i,v in in ipairs(zipCode) do
        v

        bars = []
        if(v == "0") then
            bars..("|")
            bars..("|")
            bars..(":")
            bars..(":")
            bars..(":")

        else:
            if(v - 7 >= 0) then
                bars..("|")
                v = v - 7
            else:
                bars..(":")
			end
			
            if(v - 4 >= 0) then
                bars..("|")
                v = v - 4
            else
                bars..(":")
			end
			
            if(v - 2 >= 0) then
                bars..("|")
                v = v - 2
            else
                bars..(":")
			end
			
            if(v - 1 >= 0) then
                bars..("|")
                v = v - 1
            else
                bars..(":")
			end
			
            if(x == "2" or x == "1" or x == "4" or x == "7") then
                bars..("|")
            else
                bars..(":")
			end
			
        code..bars

	end
    result = []

	print(code)
    print("|",end="")
    --for l in code:
        --for b in l:
        --    print(b,end="") 
    --print("|")

    --print("||:|:::|:|:||::::::||:|::|:::|||")
end

zip = {8,4,0,2,5}
printBarCode(zip)