Activations = {}

Activations.identity = function(x)
    return x
end

Activations.sigmoid = function(x)
    return 1 / (1 + math.exp(-x))
end

Activations.tanh = function(x)
    return math.tanh(x)
end

Activations.relu = function(x)
    return math.max(0, x)
end

Activations.leaky_relu = function(x)
    return math.max(0.01 * x, x)
end

Activations.binary_step = function(x)
    return x > 0 and 1 or 0
end

return Activations