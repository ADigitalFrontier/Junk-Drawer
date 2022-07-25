Model = {}
Model.__index = Model

function Model:new(toClone)
    if toClone ~= nil then
        -- deep copy
        local model = {
            in_x = nil,
            in_y = nil,
            out_hue = nil,
            out_sat = nil,
            out_light = nil,
            nodes = {},
            connections = {}
        }

        for i,v in ipairs(toClone.nodes) do
            table.insert(model.nodes, Node:new(v))
        end

        for i,v in ipairs(toClone.connections) do
            table.insert(model.connections, Connection:new(v))
        end
    else
        local model = {
            in_x = nil,
            in_y = nil,
            out_hue = nil,
            out_sat = nil,
            out_light = nil,
            nodes = {},
            connections = {}
        }
        setmetatable(model, Model)
        return model
    end
end

function Model:run(input)
    for row = 1, #input do
        for col = 1, #input[row] do
            self.in_y = (row-0.5)/#input
            self.in_x = (col-0.5)/#input[row]
            self:evaluate()
        end
    end
end

function Model:evaluate()

end