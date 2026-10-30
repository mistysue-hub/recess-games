# Pixel Forge — Lua & LÖVE Cheat Sheet

Keep this open in a tab. Everything here is used somewhere in the course.

## Lua basics

| Want to | Write |
|---|---|
| Make a variable | `score = 0` |
| A variable that only lives in this block | `local rock = {}` |
| A comment (ignored by Lua) | `-- like this` |
| Text | `"hello"` |
| Glue text together | `"score: " .. score` |
| A table with named fields | `ship = { x = 10, y = 20 }` |
| Read a field | `ship.x` |
| An empty list | `rocks = {}` |
| Add to the end of a list | `table.insert(rocks, rock)` |
| Remove position i from a list | `table.remove(rocks, i)` |
| How many items in a list | `#rocks` |
| The item at position i (first is 1) | `rocks[i]` |
| Ask a question | `if x > 5 then ... end` |
| Two choices | `if ... then ... else ... end` |
| Several choices | `if ... then ... elseif ... then ... else ... end` |
| Is equal to / is not equal to | `==` / `~=` |
| Both true / either true / flip it | `and` / `or` / `not` |
| Loop over every item in a list | `for i, rock in ipairs(rocks) do ... end` |
| Count from a to b | `for i = 1, 10 do ... end` |
| Count down | `for i = #rocks, 1, -1 do ... end` |
| Leave a loop early | `break` |
| Define a function | `function overlaps(a, b) ... return true end` |
| Call a function that belongs to a table | `sound:play()` |
| Part of a string, positions a to b | `string.sub(s, a, b)` |
| How many characters in a string | `#s` |
| Try something that might fail, without crashing | `local ok, result = pcall(love.graphics.newImage, path)` |
| Split a file into lines | `for line in text:gmatch("[^\n]+") do ... end` |

**One equals sign sets. Two compare.** `x = 5` stores 5. `x == 5` asks "is x 5?"

## Math

| Want to | Write |
|---|---|
| Random whole number from a to b | `math.random(a, b)` |
| Random position in a list | `list[math.random(#list)]` |
| The smaller of two numbers | `math.min(a, b)` |
| The larger of two numbers | `math.max(a, b)` |
| Keep x between low and high | `x = math.max(low, math.min(high, x))` |
| Chop off decimals | `math.floor(3.7)` → 3 |
| Absolute value | `math.abs(-4)` → 4 |
| Square root | `math.sqrt(16)` → 4 |
| Distance between two points | `math.sqrt((x2 - x1)^2 + (y2 - y1)^2)` |
| Pi | `math.pi` |
| Sine and cosine of an angle (radians) | `math.sin(a)`, `math.cos(a)` |
| Round to nearest whole number | `math.floor(x + 0.5)` |

## LÖVE: the loop

```lua
function love.load() end         -- once, at start
function love.update(dt) end     -- every frame; dt = seconds since last frame
function love.draw() end         -- every frame, after update
function love.keypressed(key) end  -- once per key press
function love.mousepressed(x, y, button) end  -- once per click
```

Always multiply a speed by `dt`: `x = x + speed * dt`.

## LÖVE: drawing

The window is 800 wide and 600 tall unless you change it. `0, 0` is the top-left. `y` grows downward.

| Want to | Write |
|---|---|
| Set the color (red, green, blue, each 0 to 1) | `love.graphics.setColor(1, 0.5, 0)` |
| Back to plain white (do this before drawing images) | `love.graphics.setColor(1, 1, 1)` |
| Rectangle | `love.graphics.rectangle("fill", x, y, w, h)` |
| Outline only | `love.graphics.rectangle("line", x, y, w, h)` |
| Circle | `love.graphics.circle("fill", x, y, radius)` |
| Triangle or any shape | `love.graphics.polygon("fill", x1, y1, x2, y2, x3, y3)` |
| Line | `love.graphics.line(x1, y1, x2, y2)` |
| Text | `love.graphics.print("hi", x, y)` |
| Load an image (in load, once) | `img = love.graphics.newImage(pathToPng)` with the path in quotes, like the one in Build Log 03 |
| Draw an image | `love.graphics.draw(img, x, y)` |
| Draw an image scaled | `love.graphics.draw(img, x, y, 0, scaleX, scaleY)` |
| Image size | `img:getWidth()`, `img:getHeight()` |
| Make a font (in load, once) | `bigFont = love.graphics.newFont(40)` |
| Use a font | `love.graphics.setFont(bigFont)` |
| Draw something rotated | `love.graphics.push()` `love.graphics.translate(x, y)` `love.graphics.rotate(angle)` `-- draw at 0, 0 --` `love.graphics.pop()` |
| Window title | `love.window.setTitle("Meteor Drift")` |
| Window size (in load) | `love.window.setMode(800, 600)` |

## LÖVE: input, sound, misc

| Want to | Write |
|---|---|
| Is a key held right now | `love.keyboard.isDown("left")` |
| Key names | `"left" "right" "up" "down" "space" "escape" "a" "p" "return"` |
| Mouse position | `love.mouse.getX()`, `love.mouse.getY()` |
| Load a sound (in load, once) | `snd = love.audio.newSource("assets/fuel.wav", "static")` |
| Play it | `snd:play()` |
| Quit the game | `love.event.quit()` |
| Seconds since the game started | `love.timer.getTime()` |

## LÖVE: physics (Builds 10-11)

| Want to | Write |
|---|---|
| Make a world with gravity (pixels per meter first) | `love.physics.setMeter(64)` then `world = love.physics.newWorld(0, 9.8 * 64)` |
| Step the world (in update) | `world:update(dt)` |
| A body that never moves / falls / is pushed by you | `love.physics.newBody(world, x, y, "static")`, `"dynamic"`, `"kinematic"` |
| A shape | `love.physics.newRectangleShape(w, h)`, `love.physics.newCircleShape(r)` |
| Glue shape to body (density last) | `love.physics.newFixture(body, shape, 1)` |
| Where and how tilted a body is | `body:getX()`, `body:getY()`, `body:getAngle()` |
| Push a body | `body:applyForce(fx, fy)`, `body:setLinearVelocity(vx, vy)` |
| Know when things touch | `world:setCallbacks(beginContact)` with `function beginContact(a, b, contact) end` |
| Connect two bodies | `love.physics.newDistanceJoint(bodyA, bodyB, x1, y1, x2, y2)`, `love.physics.newRevoluteJoint(bodyA, bodyB, x, y)` |

## LÖVE: files and saving

| Want to | Write |
|---|---|
| Save text (goes in LÖVE's save folder, not your game folder) | `love.filesystem.write("best.txt", tostring(best))` |
| Read it back (nil if missing) | `local text = love.filesystem.read("best.txt")` |
| Text to number | `tonumber(text)` |
| Draw an image slice (sprite sheet) | `quad = love.graphics.newQuad(x, y, w, h, img:getWidth(), img:getHeight())` then `love.graphics.draw(img, quad, x, y)` |

## Reading an error

LÖVE shows a blue screen. The first line names the file and line number, like `main.lua:27:`. Go to that line.

| Error says | Usually means |
|---|---|
| `attempt to index a nil value` | You used `thing.x` but `thing` doesn't exist yet (typo, or made in the wrong place) |
| `attempt to compare number with nil` | A field is missing, like a rock with no `speed` |
| `attempt to perform arithmetic on a nil value` | Same idea: a number you're adding doesn't exist |
| `'end' expected` | A block (`if`, `for`, `function`) isn't closed |
| `'then' expected` | An `if` line is missing `then`, or has `=` instead of `==` |
| `attempt to call a nil value` | You called a function that doesn't exist (check the spelling and capitals) |

## AABB overlap (copy once, use forever)

```lua
function overlaps(a, b)
  return a.x < b.x + b.w and b.x < a.x + a.w
     and a.y < b.y + b.h and b.y < a.y + a.h
end
```

*Written for Pixel Forge. Original text; LÖVE function names are the framework's public API.*
