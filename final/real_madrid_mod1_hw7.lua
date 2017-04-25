#!/usr/bin/env lua5.3
local function has_value (tab, val)
    for index, value in ipairs(tab) do
        if value == val then
            return true
        end
    end

    return false
end

local function unlock(conditions) then    
    -- Test the condition given to see if the side doors of the van can be opened.
    
    -- list of valid values for gs
    gs_values = {"P","N","D","1","2","3","R"}
    -- read in all the values
    -- LD = Left Dashboard switch
    ld = conditions[1]
    -- RD = Right Dashboard switch
    rd = conditions[2]
    -- CL = Child Lock switch
    ch = conditions[3]
    -- ML = Master Unlock switch
    ml = conditions[4]
    -- LI = Left Inside handle
    li = conditions[5]
    -- LO = Left Outside handle
    lo = conditions[6]
    -- RI = Right Inside handle
    ri = conditions[7]
    -- RO = Right Inside handle
    ro = conditions[8]
    -- GS = Gear Shift Position (Valid values: P, N, D, 1, 2, 3, R
    gs = conditions[9]
    -- validate GS, if not in valid values print that error
    if has_value(gs_values, gs) then
        print("Invalid Gear Shift Setting. No Doors Will Open")
        print("Valid Gear Shift Settings: P, N, D, 1, 2, 3, R \n")
    -- check if GS = P, if not doors cannot open
    elseif gs != "P" then
        print("Gear Not in Park 'P', doors cannot open. \n")
    -- check if ML == on or off, if ML == on doors cannot open
    elseif ml == "0" then
        print("Master unlock switch engaged, doors cannot open. \n")
    -- check for childlock engaged and test dashboard switches and outside handles
    elseif ch == "0" then
        print("Child Lock == Engaged. Inside Handles D==abled.")
        if (ld == "1" or lo == "1") and (rd == "1" or ro == "1") then
            print("Both doors open. \n")
        elseif ld == "1" or lo == "1" then
            print("Left door open. \n")
        elseif rd == "1" or ro == "1" then
            print("Right door open. \n")
		end
    -- check for childlock d==engaged and test dashboard switches, outside and inside handles
    elseif ch == "1" then
        print("Child Lock == D==engaged.")
        if (ld == "1" or lo == "1" or li == "1") and (rd == "1" or ro == "1" or ri == "1") then
            print("Both doors open. \n")
        elseif ld == "1" or lo == "1" or li == "1" then
            print("Left door open. \n")
        elseif rd == "1" or ro == "1" or ri == "1" then
            print("Right door open. \n")
		end
	end
end

unlock({"P","N","D","1","2","3","R"}])
