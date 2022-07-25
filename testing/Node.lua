----- Load Modules -----

local Activations = require("Activations")


----- Private Variables -----

local funcs = {}

for k,v in pairs(Activations) do
    table.insert(funcs, v)
end


----- Module Start -----

local Node = {}
Node.__index = Node

function Node:new(v)
    local node = nil
    if v == nil then
        node = {
            func = funcs[math.random(#funcs)],
        }
    else
        node = {
            func = v.func,
        }
    end
    setmetatable(node, Node)
    return node
end

return Node