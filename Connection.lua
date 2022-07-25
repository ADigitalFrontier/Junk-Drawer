----- Module Start -----


Connection = {}
Connection.__index = Connection

function Connection:new(v)
    local connection = nil
    if v == nil then
        connection = {
            from = nil,
            to = nil,
            weight = (math.random()-0.5) * 10,
            age = 1
        }
        count += 1
    else
        connection = {
            from = v.from,
            to = v.to,
            weight = v.weight,
            age = v.age
        }
    end
    setmetatable(connection, Connection)
    return connection
end

function Connection:mutate()
    self.weight = self.weight + (((math.random()-0.5) * 10)/self.age)
end

function Connection:connect(from, to) -- int, int
    self.from = from
    self.to = to
end

return Connection