function getFacePos(c, face)
    face = string.lower(face)

    if face == 'front' then
        return (c.CFrame * CFrame.new(0, 0, -c.Size.Z/2)).Position
    elseif face == 'back' then
        return (c.CFrame * CFrame.new(0, 0, c.Size.Z/2)).Position
    elseif face == 'top' then
        return (c.CFrame * CFrame.new(0, c.Size.Y/2, 0)).Position
    elseif face == 'bottom' then
        return (c.CFrame * CFrame.new(0, -c.Size.Y/2, 0)).Position
    elseif face == 'right' then
        return (c.CFrame * CFrame.new(c.Size.X/2, 0, 0)).Position
    elseif face == 'left' then
        return (c.CFrame * CFrame.new(-c.Size.X/2, 0, 0)).Position
    else
        error("Please provide a valid face.")
    end
end

function getFaceDiameter(c, face)
    face = string.lower(face)
    local width, height

    if face == 'front' or face == 'back' then
        width, height = c.Size.X, c.Size.Y
    elseif face == 'top' or face == 'bottom' then
        width, height = c.Size.X, c.Size.Z
    elseif face == 'right' or face == 'left' then
        width, height = c.Size.Y, c.Size.Z
    else
        error("Please provide a valid face.")
    end

    return math.min(width, height)
end

function makeCylinder(parent, c1pos, c2pos, diameter, color, material)
    local part = Instance.new("Part", parent)
    part.Shape = "Cylinder"
    part.Material = material
    part.Color = color
    part.Anchored = true

    local length = (c2pos - c1pos).Magnitude
    part.Size = Vector3.new(length, diameter, diameter)

    local orientation = CFrame.new(c1pos:Lerp(c2pos, 0.5), c2pos) * CFrame.Angles(0, math.pi / 2, 0)
    part.CFrame = orientation
end

function connectCylinder(c1, c2, face1, face2)
    local c1rad = getFaceDiameter(c1, face1)
    local c2rad = getFaceDiameter(c2, face2)

    local c1conpos = getFacePos(c1, face1)
    makeBall(workspace, c1conpos, c1rad, c1.Color, c1.Material)

    local c2conpos = getFacePos(c2, face2)
    makeBall(workspace, c2conpos, c2rad, c2.Color, c2.Material)

    local cylinderDiameter = math.min(c1rad, c2rad)
    makeCylinder(workspace, c1conpos, c2conpos, cylinderDiameter, c1.Color, c1.Material)
end

connectCylinder(workspace.Pipe3a, workspace.Pipe3b, "Bottom", "Top")
