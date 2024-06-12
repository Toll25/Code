
-- Define the colors with their RGB values
local colors = {
    white = {249, 255, 254},
    light_gray = {157, 157, 151},
    gray = {71, 79, 82},
    black = {29, 29, 33},
    brown = {131, 84, 50},
    red = {176, 46, 38},
    orange = {249, 128, 29},
    yellow = {254, 216, 61},
    lime = {128, 199, 31},
    green = {94, 124, 22},
    cyan = {22, 156, 156},
    light_blue = {58, 179, 218},
    blue = {60, 68, 170},
    purple = {137, 50, 184},
    magenta = {199, 78, 189},
    pink = {243, 139, 170}
}

-- Function to calculate color distance
local function color_distance(c1, c2)
    local sum = 0
    for i = 1, 3 do
        sum = sum + (c1[i] - c2[i]) ^ 2
    end
    return math.sqrt(sum)
end

-- Function to calculate the resulting color based on panes
local function calculate_color(panes)
    local n = #panes
    if n == 0 then
        return {0, 0, 0}
    end

    local sum_colors = {0, 0, 0}

    for i = 2, n do
        local weight = 2 ^ (i - 2)
        for j = 1, 3 do
            sum_colors[j] = sum_colors[j] + weight * colors[panes[i]][j]
        end
    end

    for j = 1, 3 do
        sum_colors[j] = sum_colors[j] + colors[panes[1]][j]
    end

    local scaling_factor = 1 / (2 ^ (n - 1))

    local final_color = {0, 0, 0}
    for j = 1, 3 do
        final_color[j] = scaling_factor * sum_colors[j]
    end

    return final_color
end

-- Function to approximate the color
local function approximate_color(target_color)
    local color_keys = {}
    for k, _ in pairs(colors) do
        table.insert(color_keys, k)
    end

    local most_similar = nil
    local smallest_distance = math.huge

    for num_panes = 1, 4 do
        local combo_indices = {}
        for i = 1, num_panes do
            combo_indices[i] = i
        end

        repeat
            local combo = {}
            for _, idx in ipairs(combo_indices) do
                table.insert(combo, color_keys[idx])
            end

            if #combo > 1 then
                local unique_colors = {}
                for _, col in ipairs(combo) do
                    unique_colors[col] = true
                end
                if #combo == #unique_colors then
                    local dist = color_distance(target_color, calculate_color(combo))
                    if dist < smallest_distance then
                        smallest_distance = dist
                        most_similar = combo
                    end
                end
            else
                local dist = color_distance(target_color, calculate_color(combo))
                if dist < smallest_distance then
                    smallest_distance = dist
                    most_similar = combo
                end
            end
        until not next(combo_indices)
    end

    return most_similar
end

-- Function to print the final result
local function print_for_color(hex_color)
    local red = (hex_color >> 16) & 0xFF
    local green = (hex_color >> 8) & 0xFF
    local blue = hex_color & 0xFF

    local target_color = {red, green, blue}

    local approx_color = approximate_color(target_color)
    local calculated_color = calculate_color(approx_color)

    print("Target Color:", table.concat(target_color, ", "))
    print("Calculated Color:", table.concat(calculated_color, ", "))
    print("Final Panes:", table.concat(approx_color, ", "))
end

-- Example usage:
print_for_color(0x1DB954)


